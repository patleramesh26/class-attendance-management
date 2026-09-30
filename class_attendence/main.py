# main.py
# This is the main file. Run THIS file to start the program.
# It imports the option functions from the other files and shows the menu.

from student import add_student, view_students, search_student
from attendance import mark_attendance, view_attendance


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
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


# Start the program
main()