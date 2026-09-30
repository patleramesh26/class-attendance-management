# student.py
# This file has the functions for adding, viewing, and searching students.

from data import students


# Option 1: Add a Student
def add_student():
    print("\n--- Add Student ---")

    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    branch = input("Enter branch: ")

    # Create a dictionary for this one student
    student = {
        "name": name,
        "id": student_id,
        "branch": branch,
        "attendance": []  # starts empty because no class has happened yet
    }

    students.append(student)
    print("Student added successfully!")


# Option 2: View All Students
def view_students():
    print("\n--- All Students ---")

    if len(students) == 0:
        print("No students registered yet.")
        return

    for student in students:
        print("ID:", student["id"], "| Name:", student["name"], "| Branch:", student["branch"])


# Option 5: Search a Student by ID
def search_student():
    print("\n--- Search Student ---")

    student_id = input("Enter student ID to search: ")

    found = False

    for student in students:
        if student["id"] == student_id:
            print("\nStudent found!")
            print("Name:", student["name"])
            print("ID:", student["id"])
            print("Branch:", student["branch"])

            # Show the attendance information too
            total = len(student["attendance"])

            present = 0
            for mark in student["attendance"]:
                if mark == "Present":
                    present = present + 1

            print("Total classes:", total)
            print("Classes attended:", present)

            if total > 0:
                percentage = (present / total) * 100
                print("Attendance percentage:", round(percentage, 2), "%")
            else:
                print("No attendance marked yet.")

            found = True

    if not found:
        print("Student not found.")