import os

FILE_NAME = "students.txt"


def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{student_id},{name},{age},{course}\n")

    print("Student added successfully!")


def view_students():
    if not os.path.exists(FILE_NAME):
        print("No student records found.")
        return

    with open(FILE_NAME, "r") as file:
        students = file.readlines()

    if not students:
        print("No student records found.")
        return

    print("\nStudent Records")
    print("-" * 50)

    for student in students:
        student_id, name, age, course = student.strip().split(",")

        print(
            f"ID: {student_id} | "
            f"Name: {name} | "
            f"Age: {age} | "
            f"Course: {course}"
        )


def search_student():
    search_id = input("Enter Student ID to search: ")

    if not os.path.exists(FILE_NAME):
        print("No student records found.")
        return

    with open(FILE_NAME, "r") as file:
        for student in file:
            student_id, name, age, course = student.strip().split(",")

            if student_id == search_id:
                print("\nStudent Found")
                print("ID     :", student_id)
                print("Name   :", name)
                print("Age    :", age)
                print("Course :", course)
                return

    print("Student not found.")


def update_student():
    update_id = input("Enter Student ID to update: ")

    if not os.path.exists(FILE_NAME):
        print("No student records found.")
        return

    with open(FILE_NAME, "r") as file:
        students = file.readlines()

    found = False

    for i in range(len(students)):
        student_id, name, age, course = students[i].strip().split(",")

        if student_id == update_id:
            new_name = input("Enter new name: ")
            new_age = input("Enter new age: ")
            new_course = input("Enter new course: ")

            students[i] = (
                f"{student_id},{new_name},{new_age},{new_course}\n"
            )

            found = True
            break

    if found:
        with open(FILE_NAME, "w") as file:
            file.writelines(students)

        print("Student updated successfully!")
    else:
        print("Student not found.")


def delete_student():
    delete_id = input("Enter Student ID to delete: ")

    if not os.path.exists(FILE_NAME):
        print("No student records found.")
        return

    with open(FILE_NAME, "r") as file:
        students = file.readlines()

    new_students = []
    found = False

    for student in students:
        student_id = student.strip().split(",")[0]

        if student_id == delete_id:
            found = True
        else:
            new_students.append(student)

    if found:
        with open(FILE_NAME, "w") as file:
            file.writelines(new_students)

        print("Student deleted successfully!")
    else:
        print("Student not found.")


def main():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")

            main()
