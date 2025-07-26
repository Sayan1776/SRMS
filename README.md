📘 Student Record Management System (SRMS)



📄 Overview

The Student Record Management System (SRMS) is a Python-based application that enables structured storage, retrieval, grading, editing, and deletion of student academic records using individual JSON files per student. It is designed to be lightweight, modular, and terminal-friendly — suitable for use in schools, colleges, or training institutes.


🛠 Features
1. Add new student records with semester-wise subject marks
2. View full academic records by roll number
3. Edit student information (name, department, year, marks)
4. Delete student records by roll number
5. Categorize students based on average marks (Distinction / Pass / Fail)
6. View grading summary with student counts and average scores
7. All records stored in structured JSON files under the /students/ directory


📁 File Structure

SRMS/
├── students_utils.py         # Main logic file containing all functions
├── students/                 # Folder to store individual student .json files
│   ├── 231047.json
│   ├── 231048.json
│   └── ...


🔍 Functional Breakdown

1. add_student()
Prompts the user for:

Roll number, Name, Department, Academic Year (1–4)
For each completed semester (based on year), accepts subject-wise marks (0–100)
Stores this structured data in a JSON file under students/{roll}.json.

2. load_student(roll)
Retrieves and displays a student’s full academic record by roll number, showing:
Name, Department, Year
Semester-wise subject marks

3. save_grade_summary()
Traverses all student files and calculates average marks for each student:
Classifies into: Distinction (≥75), Passed (40–74.9), or Failed (<40)
Displays all classifications and a detailed breakdown with average scores
Handles invalid/malformed files gracefully

4. edit_student()

Allows editing of:

    Name
    Department
    Academic Year
    Semester-wise marks (add/edit)
    Changes are saved back to the respective JSON file.

5. delete_student()
Allows deletion of a student record by roll number, with confirmation prompt. Removes the corresponding JSON file from the students directory.

6. CLI Interface (__main__)
Offers a simple command-line interface:

    1. Add student
    2. View student record
    3. View grading summary
    4. Edit student record
    5. Delete student record
    6. Exit


🧩 Future Improvements (Optional)

1. Export to CSV or PDF
2. GUI interface with Tkinter or PyQt
3. Search by name/department
4. Subject-wise performance reports
5. Cloud integration for data backup

👨‍💻 Author: Sayan Paul
   - Built during Python + Data Science Training
     Project started: July 2025