import tkinter as tk 
from tkinter import ttk
import csv 
from tkinter import messagebox

class Student:
    def __init__(self, student_id, name, gender, program, gpa, attendance, fee_status):
        self.student_id = student_id
        self.name = name
        self.gender = gender
        self.program = program
        self.gpa = gpa
        self.attendance = attendance
        self.fee_Status = fee_status

class StudentManager:
    def __init__(self):
        self.students = []
        
    def add_students(self, student):
        self.students.append(student)

    def delete_students(self, student_id):
        self.students = [s for s in self.students if str(s.student_id).strip() != str(student_id).strip()]

    def search_students(self, student_id):
        for s in self.students:
            if str(s.student_id).strip() == str(student_id).strip():
                return s
        return None

    def display_students(self):
        return self.students


class StudentGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1200x700")
        self.root.config(bg="#1E1E2F")
        self.manager = StudentManager()

        tk.Label(self.root, text="STUDENT MANAGEMENT SYSTEM", font=("Arial", 24, "bold"), bg="#1E1E2F", fg="white").pack(pady=20)
        form_frame = tk.Frame(self.root, bg="#2C2F48", bd=3, relief="ridge")
        form_frame.pack(fill="x", padx=20, pady=15)

        tk.Label(form_frame, text="Student ID:", bg="#2C2F48", fg="white", font=("Arial", 11, "bold")).grid(row=0, column=0, padx=10, pady=8, sticky="w")
        self.id_entry = tk.Entry(form_frame, width=30)
        self.id_entry.grid(row=0, column=1, padx=10, pady=8)

        tk.Label(form_frame, text="Name:", bg="#2C2F48", fg="white", font=("Arial", 11, "bold")).grid(row=1, column=0, padx=10, pady=8, sticky="w")
        self.name_entry = tk.Entry(form_frame, width=30)
        self.name_entry.grid(row=1, column=1, padx=10, pady=8)
    
        tk.Label(form_frame, text="Gender:", bg="#2C2F48", fg="white", font=("Arial", 11, "bold")).grid(row=2, column=0, padx=10, pady=8, sticky="w")
        self.gender_combo = ttk.Combobox(form_frame, values=["Male", "Female"], state="readonly", width=28)
        self.gender_combo.grid(row=2, column=1, padx=10, pady=8)

        tk.Label(form_frame, text="Program:", bg="#2C2F48", fg="white", font=("Arial", 11, "bold")).grid(row=3, column=0, padx=10, pady=8, sticky="w")
        self.program_combo = ttk.Combobox(form_frame, values=["FA", "ICS", "FSc Pre-Medical", "I.Com", "FSc Pre-Engineering"], state="readonly", width=28)
        self.program_combo.grid(row=3, column=1, padx=10, pady=8)

        tk.Label(form_frame, text="GPA:", bg="#2C2F48", fg="white", font=("Arial", 11, "bold")).grid(row=4, column=0, padx=10, pady=8, sticky="w")
        self.gpa_entry = tk.Entry(form_frame, width=30)
        self.gpa_entry.grid(row=4, column=1, padx=10, pady=8)

        tk.Label(form_frame, text="Attendance:", bg="#2C2F48", fg="white", font=("Arial", 11, "bold")).grid(row=5, column=0, padx=10, pady=8, sticky="w")
        self.attendance_entry = tk.Entry(form_frame, width=30)
        self.attendance_entry.grid(row=5, column=1, padx=10, pady=8)

        tk.Label(form_frame, text="Fee Status:", bg="#2C2F48", fg="white", font=("Arial", 11, "bold")).grid(row=6, column=0, padx=10, pady=8, sticky="w")
        self.fee_combo = ttk.Combobox(form_frame, values=["Paid", "Outstanding", "Partial"], state="readonly", width=28)
        self.fee_combo.grid(row=6, column=1, padx=10, pady=8)

        btn_frame = tk.Frame(self.root, bg="#1E1E2F")
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Add", bg="#28A745", fg="white", font=("Arial", 10, "bold"), width=12, command=self.add_student_gui).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Search", bg="#007BFF", fg="white", font=("Arial", 10, "bold"), width=12, command=self.search_student_gui).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Delete", bg="#DC3545", fg="white", font=("Arial", 10, "bold"), width=12, command=self.delete_student_gui).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Save to CSV", bg="#17A2B8", fg="white", font=("Arial", 10, "bold"), width=12, command=self.save_to_csv_gui).grid(row=0, column=3, padx=5)
        tk.Button(btn_frame, text="Clear", bg="#A61C1C", fg="white", font=("Arial", 10, "bold"), width=13, command=self.clear_fields).grid(row=0, column=4, padx=5)

        table_frame = tk.Frame(self.root, bg="#1E1E2F")
        table_frame.pack(fill="both", expand=True, padx=20, pady=10)

        columns = ("ID", "Name", "Gender", "Program", "GPA", "Attendance", "Fee_Status")
        self.student_table = ttk.Treeview(table_frame, columns=columns, show="headings")
        
        self.student_table.heading("ID", text="Student ID")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("Program", text="Program")
        self.student_table.heading("GPA", text="GPA")
        self.student_table.heading("Attendance", text="Attendance")
        self.student_table.heading("Fee_Status", text="Fee Status")

        for col in columns:
            self.student_table.column(col, anchor="center", width=120)
        
        self.student_table.pack(fill="both", expand=True)

        self.load_csv_data()

    def clear_fields(self):
        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.gpa_entry.delete(0, tk.END)
        self.attendance_entry.delete(0, tk.END)
        self.gender_combo.set("")
        self.program_combo.set("")
        self.fee_combo.set("")

    def delete_student_gui(self):
        selected_item = self.student_table.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a student row to delete!")
            return

        row_values = self.student_table.item(selected_item, "values")
        s_id = row_values[0] 
        name = row_values[1] 
        
        self.manager.delete_students(s_id)
        self.student_table.delete(selected_item)
        self.clear_fields()
        messagebox.showinfo("Deleted", f"Student '{name}' removed successfully from interface view!")

    def search_student_gui(self):
        s_id = self.id_entry.get().strip()
        if not s_id:
            messagebox.showwarning("Warning", "Please enter a Student ID to search!")
            return
            
        student = self.manager.search_students(s_id)
        if not student:
            messagebox.showinfo("Not Found", f"No student found with ID: {s_id}")
            return
    
        self.clear_fields()
        self.id_entry.insert(0, str(student.student_id))
        self.name_entry.insert(0, student.name)
        self.gender_combo.set(student.gender)
        self.program_combo.set(student.program)
        self.gpa_entry.insert(0, str(student.gpa))
        self.attendance_entry.insert(0, str(student.attendance))
        self.fee_combo.set(student.fee_Status)

    def add_student_gui(self):
        s_id = self.id_entry.get().strip()
        name = self.name_entry.get().strip()
        gender = self.gender_combo.get()
        program = self.program_combo.get()
        gpa = self.gpa_entry.get().strip()
        attendance = self.attendance_entry.get().strip()
        fee = self.fee_combo.get()

        if not s_id or not name:
            messagebox.showerror("Error", "Student ID and Name are required!")
            return 

        new_student = Student(s_id, name, gender, program, gpa, attendance, fee)
        self.manager.add_students(new_student)
        self.student_table.insert("", "end", values=(s_id, name, gender, program, gpa, attendance, fee))

        messagebox.showinfo("Success", "Student added successfully to layout view!")
        self.clear_fields()

    def save_to_csv_gui(self):
        try:
            with open("Organized_Students_Data.csv", mode="w", newline="", encoding="utf-8") as file:
                fieldnames = ["Student ID", "Name", "Gender", "Program", "GPA", "Attendance_Percentage", "Fee_Status"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                
                all_students = self.manager.display_students()
                for student in all_students:
                    writer.writerow({
                        "Student ID": student.student_id,
                        "Name": student.name,
                        "Gender": student.gender,
                        "Program": student.program,
                        "GPA": student.gpa,
                        "Attendance_Percentage": student.attendance,
                        "Fee_Status": student.fee_Status
                    })
            messagebox.showinfo("Saved", "All changes have been permanently saved to the CSV file!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save data: {str(e)}")

    def load_csv_data(self):
        try:
            with open("Organized_Students_Data.csv", mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student = Student(
                        student_id=row["Student ID"],
                        name=row["Name"],
                        gender=row["Gender"],
                        program=row["Program"],
                        gpa=row["GPA"],
                        attendance=row["Attendance_Percentage"],    
                        fee_status=row["Fee_Status"]
                    )
                    self.manager.add_students(student)
                    self.student_table.insert("", "end", values=(
                        student.student_id, student.name, student.gender, 
                        student.program, student.gpa, student.attendance, student.fee_Status
                    ))
        except FileNotFoundError:
            print("Notice: 'Organized_Students_Data.csv' file not found. Starting with clean list.")


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentGUI(root)
    root.mainloop()