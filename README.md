
# College Attendance Manager

A simple console-based (command-line) Python program to **register students** and **mark / track their attendance**.

The program uses a text menu. You can add students, view the student list, mark a student as **Present** or **Absent**, view the full attendance record with percentages, and search for a student by ID.

---

## Features

The program provides a menu with the following options:

| Option | Action |
|--------|--------|
| 1 | Add Student |
| 2 | View Students |
| 3 | Mark Attendance |
| 4 | View Attendance |
| 5 | Search Student |
| 6 | Exit |

1. **Add Student** – Enter the student's name, ID, and branch. The student is added to the list with an empty attendance record.
2. **View Students** – Show the ID, name, and branch of every registered student.
3. **Mark Attendance** – Pick a student from the numbered list and enter `P` (Present) or `A` (Absent).
4. **View Attendance** – Show every student's total classes, classes attended, and attendance percentage.
5. **Search Student** – Find a student by ID and show their details and attendance summary.
6. **Exit** – End the program.

---

## Requirements

- **Python 3** (any recent version)
- No external libraries or packages are needed. The program uses only Python's built-in `input()` / `print()` functions and standard data structures.

---

## How to Run

### Option A – Modular version (recommended)

Run the `main.py` file:

```text
python main.py
```

### Option B – Standalone version

Run the single-file version (everything is inside one file):

```text
python college_attendance_manager.py
```

> Both versions work exactly the same way. The modular version splits the code into separate files for easier learning.

---

## Project Structure

| File | Purpose |
|------|---------|
| `main.py` | Entry point. Shows the menu, takes the user's choice, and calls the matching function. **Run this file to start the program.** |
| `student.py` | Functions for **Option 1** (add student), **Option 2** (view students), and **Option 5** (search student). |
| `attendance.py` | Functions for **Option 3** (mark attendance) and **Option 4** (view attendance record). |
| `data.py` | Stores the shared `students` list. Every file imports this same list, so all modules work on one set of data. |
| `college_attendance_manager.py` | A standalone single-file version of the same program. |

---

## How It Works

- **Data storage:** All students live in one list called `students` (defined in `data.py`).
- Each student is a **dictionary** with four keys:

| Key | Meaning |
|-----|---------|
| `name` | The student's name |
| `id` | The student's ID number |
| `branch` | The student's branch (e.g., CS, EC, ME) |
| `attendance` | A list that stores `"Present"` or `"Absent"` for every class |

- When you add a student, their `attendance` list starts empty.
- Each time you mark attendance, the chosen student's `attendance` list gets one new entry (`"Present"` or `"Absent"`).
- The **attendance percentage** is calculated as:

```text
attendance % = (classes attended / total classes) x 100
```

- Data is kept **in memory only**. Closing the program clears all data (see *Limitations*).

---

## Sample Session

```text
Welcome to the College Attendance Manager!

Choose an option:
1. Add Student
2. View Students
3. Mark Attendance
4. View Attendance
5. Search Student
6. Exit
Enter your choice: 1

--- Add Student ---
Enter student name: Alice
Enter student ID: 101
Enter branch: CS
Student added successfully!

Choose an option:
1. Add Student
2. View Students
3. Mark Attendance
4. View Attendance
5. Search Student
6. Exit
Enter your choice: 3

--- Mark Attendance ---
1 . Alice
Enter the number of the student: 1
Enter 'P' for Present or 'A' for Absent: P
Attendance marked: Present

Choose an option:
1. Add Student
2. View Students
3. Mark Attendance
4. View Attendance
5. Search Student
6. Exit
Enter your choice: 4

--- Attendance Record ---

Name: Alice | ID: 101 | Branch: CS
Total classes: 1
Classes attended: 1
Attendance percentage: 100.0 %

Choose an option:
1. Add Student
2. View Students
3. Mark Attendance
4. View Attendance
5. Search Student
6. Exit
Enter your choice: 6
Goodbye!
```

---

## Input Rules

- Menu choices must be a number from `1` to `6`. Anything else shows an error and re-displays the menu.
- In **Mark Attendance**, the student's number must be a valid listed number, otherwise the program shows an error.
- Attendance status must be `P` or `A` (either uppercase or lowercase is accepted). Anything else is rejected.

---

## Limitations

- **No permanent storage:** Data is stored in memory only. Once the program closes, all students and attendance records are lost.
- **No duplicates check:** Adding a student with an ID that already exists is allowed.
- **No edit / delete options:** There is no way to remove a student or correct a wrongly marked attendance entry.

---

## Possible Future Improvements

- Save and load data using a file (JSON / CSV) or a database.
- Prevent duplicate student IDs.
- Edit and delete student records.
- Correct or re-mark attendance entries.
- Show "minimum attendance required" or flag students below a threshold.
- Add a subject/course and date to each attendance mark.
