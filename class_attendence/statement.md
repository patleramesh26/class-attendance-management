# Problem Statement — College Attendance Manager

## 1. Title

**College Attendance Manager** — a console-based program to register students and manage class attendance.

---

## 2. Objective

To build a simple Python program that helps a college/class teacher:

- Add student records (name, ID, branch).
- View the list of registered students.
- Mark each student **Present** or **Absent** for a class.
- View the complete attendance record with the attendance percentage of each student.
- Search for a student by ID and see their attendance summary.

---

## 3. Problem Description

In a college, taking and tracking attendance manually is time-consuming and error-prone. A simple automated tool is needed that:

1. Stores the details of every student.
2. Lets the user record attendance for any class quickly.
3. Automatically calculates each student's attendance percentage.
4. Allows easy lookup of any student's details and attendance.

The program must be **menu-driven**, so that a user with no technical background can operate it by selecting numbered options.

---

## 4. Functional Requirements

The program must provide the following menu options:

### Option 1 — Add Student
- Takes the student's **name**, **ID**, and **branch** as input.
- Stores the new student with an **empty attendance list**.
- Confirms with a success message.

### Option 2 — View Students
- Displays the **ID, name, and branch** of every registered student.
- If no student is registered, it prints `No students registered yet.`

### Option 3 — Mark Attendance
- Shows all registered students as a numbered list.
- Takes the number of the student to mark.
- Takes the attendance status: `P` (Present) or `A` (Absent).
- Appends `Present` / `Absent` to that student's attendance record.
- Validates input (must be a valid number; status must be `P` or `A`).

### Option 4 — View Attendance Record
- For each student, displays:
  - Name, ID, and branch
  - Total number of classes
  - Number of classes attended
  - Attendance percentage (rounded to 2 decimal places)

### Option 5 — Search Student
- Takes a student **ID** as input.
- If found, displays the student's details and attendance summary.
- If not found, prints `Student not found.`

### Option 6 — Exit
- Prints a goodbye message and ends the program.

---

## 5. Non-Functional Requirements

- **Platform:** Runs on the command line / terminal using **Python 3**.
- **Dependencies:** None — must work with only Python's built-in features.
- **Simplicity:** The interface must be text-based and easy to follow.
- **Input validation:** Invalid menu choices, invalid student numbers, and invalid attendance status must be handled gracefully without crashing.
- **Code clarity:** Code must be readable, with comments explaining each section (suitable for a beginner-level programming submission).

---

## 6. Data Model

Each student is stored as a **dictionary** inside a shared list named `students`:

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Student's name |
| `id` | string | Student's ID number |
| `branch` | string | Student's branch (e.g., CS, EC, ME) |
| `attendance` | list | Holds `"Present"` / `"Absent"` for each class |

**Attendance percentage formula:**

```text
attendance % = (number of "Present" marks / total marks) x 100
```

---

## 7. Sample Input / Output

### Sample Input (session)

```text
1                     (Add Student)
Alice
101
CS
1                     (Add Student)
Bob
102
EC
3                     (Mark Attendance)
1
P
3                     (Mark Attendance)
2
A
4                     (View Attendance)
6                     (Exit)
```

### Expected Output (relevant parts)

```text
--- Add Student ---
Student added successfully!

--- Mark Attendance ---
1 . Alice
2 . Bob
Attendance marked: Present

--- Mark Attendance ---
1 . Alice
2 . Bob
Attendance marked: Absent

--- Attendance Record ---

Name: Alice | ID: 101 | Branch: CS
Total classes: 1
Classes attended: 1
Attendance percentage: 100.0 %

Name: Bob | ID: 102 | Branch: EC
Total classes: 1
Classes attended: 0
Attendance percentage: 0.0 %

Goodbye!
```

---

## 8. Assumptions

- Student IDs are unique for the purpose of searching, but the program itself does not check for duplicates.
- Attendance is marked per class without storing the subject name or date.
- All data is kept **in memory**; it is not saved to a file after the program exits.

---

## 9. Deliverables

| File | Description |
|------|-------------|
| `main.py` | Main menu / entry point of the modular version. |
| `student.py` | Add, view, and search student functions. |
| `attendance.py` | Mark and view attendance functions. |
| `data.py` | Shared student list used by all modules. |
| `college_attendance_manager.py` | Standalone single-file version of the program. |

---

## 10. Conclusion

The **College Attendance Manager** fulfills the objective by providing a simple, menu-driven way to register students, mark attendance, and view attendance percentages automatically. It is built with basic Python constructs (lists, dictionaries, functions, loops, and conditionals) and includes input validation, making it suitable as a beginner-level college project.