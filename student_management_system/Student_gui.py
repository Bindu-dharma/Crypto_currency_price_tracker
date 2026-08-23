import tkinter as tk
from tkinter import messagebox


# ---------------------------------------------------------
# WINDOW
# ---------------------------------------------------------

root = tk.Tk()
root.title("Student Management System")
root.geometry("550x700")


# ---------------------------------------------------------
# FILE NAME
# ---------------------------------------------------------

FILE_NAME = "students.txt"


# ---------------------------------------------------------
# LOAD STUDENTS FROM FILE
# ---------------------------------------------------------

def load_students():

    students = {}

    try:
        with open(FILE_NAME, "r") as file:

            for line in file:

                line = line.strip()

                if not line:
                    continue

                data = line.split(",")

                if len(data) != 4:
                    continue

                sid, name, student_age, student_course = data

                students[sid.strip()] = {
                    "name": name.strip(),
                    "age": student_age.strip(),
                    "course": student_course.strip()
                }

    except FileNotFoundError:

        # File will be created when first student is added
        pass

    return students


# Load existing students when program starts
students = load_students()


# ---------------------------------------------------------
# SAVE STUDENTS TO FILE
# ---------------------------------------------------------

def save_students():

    with open(FILE_NAME, "w") as file:

        for sid, student in students.items():

            file.write(
                f"{sid},{student['name']},{student['age']},{student['course']}\n"
            )


# ---------------------------------------------------------
# CLEAR ENTRY FIELDS
# ---------------------------------------------------------

def clear_fields():

    student_id.delete(0, tk.END)
    student_name.delete(0, tk.END)
    age.delete(0, tk.END)
    course.delete(0, tk.END)


# ---------------------------------------------------------
# ADD STUDENT
# ---------------------------------------------------------

def add_student():

    sid = student_id.get().strip()
    name = student_name.get().strip()
    student_age = age.get().strip()
    student_course = course.get().strip()

    if sid == "" or name == "" or student_age == "" or student_course == "":
        messagebox.showwarning(
            "Warning",
            "Please enter all student details."
        )
        return

    if sid in students:

        messagebox.showwarning(
            "Warning",
            "Student ID already exists."
        )
        return

    students[sid] = {
        "name": name,
        "age": student_age,
        "course": student_course
    }

    save_students()

    messagebox.showinfo(
        "Success",
        "Student added successfully!"
    )

    clear_fields()


# ---------------------------------------------------------
# SEARCH STUDENT
# ---------------------------------------------------------

def search_student():

    sid = student_id.get().strip()

    if sid == "":
        messagebox.showwarning(
            "Warning",
            "Enter Student ID to search."
        )
        return

    if sid in students:

        student = students[sid]

        student_name.delete(0, tk.END)
        student_name.insert(0, student["name"])

        age.delete(0, tk.END)
        age.insert(0, student["age"])

        course.delete(0, tk.END)
        course.insert(0, student["course"])

        messagebox.showinfo(
            "Student Found",
            f"ID: {sid}\n"
            f"Name: {student['name']}\n"
            f"Age: {student['age']}\n"
            f"Course: {student['course']}"
        )

    else:

        messagebox.showerror(
            "Not Found",
            "Student not found."
        )


# ---------------------------------------------------------
# UPDATE STUDENT
# ---------------------------------------------------------

def update_student():

    sid = student_id.get().strip()
    name = student_name.get().strip()
    student_age = age.get().strip()
    student_course = course.get().strip()

    if sid == "":
        messagebox.showwarning(
            "Warning",
            "Enter Student ID."
        )
        return

    if sid not in students:

        messagebox.showerror(
            "Not Found",
            "Student not found."
        )
        return

    if name == "" or student_age == "" or student_course == "":

        messagebox.showwarning(
            "Warning",
            "Please enter all student details."
        )
        return

    students[sid] = {
        "name": name,
        "age": student_age,
        "course": student_course
    }

    save_students()

    messagebox.showinfo(
        "Success",
        "Student details updated successfully!"
    )

    clear_fields()


# ---------------------------------------------------------
# DELETE STUDENT
# ---------------------------------------------------------

def delete_student():

    sid = student_id.get().strip()

    if sid == "":
        messagebox.showwarning(
            "Warning",
            "Enter Student ID."
        )
        return

    if sid not in students:

        messagebox.showerror(
            "Not Found",
            "Student not found."
        )
        return

    confirm = messagebox.askyesno(
        "Confirm Delete",
        f"Are you sure you want to delete student {sid}?"
    )

    if confirm:

        del students[sid]

        save_students()

        messagebox.showinfo(
            "Success",
            "Student deleted successfully!"
        )

        clear_fields()


# ---------------------------------------------------------
# VIEW ALL STUDENTS
# ---------------------------------------------------------

def view_students():

    if not students:

        messagebox.showinfo(
            "Student Records",
            "No student records found."
        )
        return

    records = ""

    for sid, student in students.items():

        records += (
            f"ID: {sid}\n"
            f"Name: {student['name']}\n"
            f"Age: {student['age']}\n"
            f"Course: {student['course']}\n"
            f"{'-' * 40}\n"
        )

    messagebox.showinfo(
        "All Student Records",
        records
    )


# ---------------------------------------------------------
# EXIT APPLICATION
# ---------------------------------------------------------

def exit_app():

    answer = messagebox.askyesno(
        "Exit",
        "Are you sure you want to exit?"
    )

    if answer:
        root.destroy()


# ---------------------------------------------------------
# GUI TITLE
# ---------------------------------------------------------

title = tk.Label(
    root,
    text="Student Management System",
    font=("Arial", 20, "bold")
)

title.pack(pady=20)


# ---------------------------------------------------------
# STUDENT ID
# ---------------------------------------------------------

tk.Label(
    root,
    text="Student ID",
    font=("Arial", 12)
).pack()

student_id = tk.Entry(
    root,
    width=35
)

student_id.pack(pady=5)


# ---------------------------------------------------------
# STUDENT NAME
# ---------------------------------------------------------

tk.Label(
    root,
    text="Student Name",
    font=("Arial", 12)
).pack()

student_name = tk.Entry(
    root,
    width=35
)

student_name.pack(pady=5)


# ---------------------------------------------------------
# AGE
# ---------------------------------------------------------

tk.Label(
    root,
    text="Age",
    font=("Arial", 12)
).pack()

age = tk.Entry(
    root,
    width=35
)

age.pack(pady=5)


# ---------------------------------------------------------
# COURSE
# ---------------------------------------------------------

tk.Label(
    root,
    text="Course",
    font=("Arial", 12)
).pack()

course = tk.Entry(
    root,
    width=35
)

course.pack(pady=5)


# ---------------------------------------------------------
# BUTTONS
# ---------------------------------------------------------

tk.Button(
    root,
    text="Add Student",
    command=add_student,
    width=25
).pack(pady=6)


tk.Button(
    root,
    text="Search Student",
    command=search_student,
    width=25
).pack(pady=6)


tk.Button(
    root,
    text="Update Student",
    command=update_student,
    width=25
).pack(pady=6)


tk.Button(
    root,
    text="Delete Student",
    command=delete_student,
    width=25
).pack(pady=6)


tk.Button(
    root,
    text="View All Students",
    command=view_students,
    width=25
).pack(pady=6)


tk.Button(
    root,
    text="Clear",
    command=clear_fields,
    width=25
).pack(pady=6)


tk.Button(
    root,
    text="Exit",
    command=exit_app,
    width=25
).pack(pady=6)


# ---------------------------------------------------------
# START APPLICATION
# ---------------------------------------------------------

root.mainloop()