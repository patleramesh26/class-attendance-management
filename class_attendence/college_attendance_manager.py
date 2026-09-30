# College Attendance Manager
# A simple console program to store students and mark their attendance.

# This list will store all the students.
# Each student is a dictionary with:
#   "name"        -> the student's name
#   "id"          -> the student's ID number
#   "branch"      -> the student's branch (like CS, EC, ME...)
#   "attendance"  -> a list that stores "Present" or "Absent" for every class
students = []


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


# Option 3: Mark Attendance
def mark_attendance():
    print("\n--- Mark Attendance ---")

    if len(students) == 0:
        print("No students registered yet.")
        return

    # Show the students with numbers, so the user can pick one
    for i in range(len(students)):
        print(i + 1, ".", students[i]["name"])

    choice = input("Enter the number of the student: ")

    # Make sure the user entered a number before we convert it
    if not choice.isdigit():
        print("Please enter a number.")
        return

    index = int(choice) - 1  # subtract 1 to get the correct list position

    if index < 0 or index >= len(students):
        print("Invalid choice.")
        return

    status = input("Enter 'P' for Present or 'A' for Absent: ")

    if status.upper() == "P":
        students[index]["attendance"].append("Present")
        print("Attendance marked: Present")
    elif status.upper() == "A":
        students[index]["attendance"].append("Absent")
        print("Attendance marked: Absent")
    else:
        print("Invalid input. Please enter P or A.")


# Option 4: View Attendance Record
def view_attendance():
    print("\n--- Attendance Record ---")

    if len(students) == 0:
        print("No students registered yet.")
        return

    for student in students:
        total = len(student["attendance"])  # total number of classes

        # Count how many times the student was Present
        present = 0
        for mark in student["attendance"]:
            if mark == "Present":
                present = present + 1

        # Attendance percentage = (classes attended / total classes) * 100
        if total > 0:
            percentage = (present / total) * 100
        else:
            percentage = 0

        print("\nName:", student["name"], "| ID:", student["id"], "| Branch:", student["branch"])
        print("Total classes:", total)
        print("Classes attended:", present)
        print("Attendance percentage:", round(percentage, 2), "%")


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


# The main menu
def main():
    print("Welcome to the College Attendance Manager!")

    while True:
        print("\nChoose an option:")
        print("1. Add Student")
        print("2. View Students")
        print("3. Mark Attendance")
        print("4. View Attendance")
        print("5. Search Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            mark_attendance()
        elif choice == "4":
            view_attendance()
        elif choice == "5":
            search_student()
        elif choice == "6":
            print("Goodbye!")
            break  # exits the while loop, which ends the program
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


# Start the program
main()