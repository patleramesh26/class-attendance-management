# attendance.py
# This file has the functions for marking and viewing attendance.

from data import students


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