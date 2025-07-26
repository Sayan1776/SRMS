import os
import json

# 🔹 Add a new student and save to a JSON file
def add_student():
    os.makedirs("students", exist_ok=True)  # Ensure the folder exists

    roll = input("Enter roll number: ").strip()
    filename = f"students/{roll}.json"

    if os.path.exists(filename):
        print("❌ Student already exists. Try a different roll number.")
        return

    name = input("Enter full name: ").strip()
    department = input("Enter department: ").strip()

    # Validate year input
    while True:
        year = input("Enter academic year (1/2/3/4): ").strip()
        if year in {"1", "2", "3", "4"}:
            break
        else:
            print("❌ Invalid year. Please enter 1, 2, 3, or 4.")

    # Mapping year to semesters completed
    year_to_semesters = {
        "1": ["Semester 1", "Semester 2"],
        "2": ["Semester 1", "Semester 2", "Semester 3", "Semester 4"],
        "3": ["Semester 1", "Semester 2", "Semester 3", "Semester 4", "Semester 5", "Semester 6"],
        "4": ["Semester 1", "Semester 2", "Semester 3", "Semester 4", "Semester 5", "Semester 6", "Semester 7", "Semester 8"]
    }

    results = {}
    for semester in year_to_semesters[year]:
        print(f"\n Enter marks for {semester}:")
        subjects = {}
        while True:
            subject = input("Enter subject name (or press Enter to finish): ").strip()
            if not subject:
                break
            try:
                marks = float(input(f"Enter marks for {subject}: ").strip())
                if 0 <= marks <= 100:
                    subjects[subject] = marks
                else:
                    print("❌ Marks should be between 0 and 100.")
            except ValueError:
                print("⚠️ Please enter numeric marks.")

        if subjects:
            results[semester] = subjects

    student_data = {
        "roll": roll,
        "name": name,
        "department": department,
        "year": year,
        "results": results
    }

    with open(filename, "w") as file:
        json.dump(student_data, file, indent=4)

    print(f"\u2705 Student record for {name} saved as {filename}")


# 🔹 View a student's details from file
def load_student(roll):
    filename = f"students/{roll}.json"
    if not os.path.exists(filename):
        print("❌ Student record not found.")
        return

    with open(filename, "r") as file:
        student = json.load(file)

    print("\n📄 Student Record:")
    print(f"Roll: {student['roll']}")
    print(f"Name: {student['name']}")
    print(f"Department: {student['department']}")
    print(f"Year: {student['year']}")
    print("Semester-wise Results:")
    for sem, subjects in student["results"].items():
        print(f"  {sem}:")
        for subject, marks in subjects.items():
            print(f"    - {subject}: {marks}")


# 🔹 Grade all students from saved files
def save_grade_summary():
    distinction = []
    passed = []
    failed = []
    invalid_entries = []

    if not os.path.exists("students"):
        print("❌ No student data found.")
        return

    for file in os.listdir("students"):
        if file.endswith(".json"):
            try:
                with open(f"students/{file}", "r") as f:
                    student = json.load(f)
                    name = student["name"]
                    results = student["results"]

                    total_marks = 0
                    total_subjects = 0

                    for sem_subjects in results.values():
                        for mark in sem_subjects.values():
                            total_marks += mark
                            total_subjects += 1

                    if total_subjects == 0:
                        raise ValueError("No subjects found.")

                    avg = total_marks / total_subjects

                    if avg >= 75:
                        distinction.append((name, avg))
                    elif avg >= 40:
                        passed.append((name, avg))
                    else:
                        failed.append((name, avg))
            except Exception as e:
                invalid_entries.append(file)

    print("\n📊 Student Grading Summary:")
    print(f"\nValid students processed: {len(distinction) + len(passed) + len(failed)}")
    print("Distinction:", ", ".join(name for name, _ in distinction) if distinction else "None")
    print("Passed:", ", ".join(name for name, _ in passed) if passed else "None")
    print("Failed:", ", ".join(name for name, _ in failed) if failed else "None")
    print("Invalid Entries:", ", ".join(invalid_entries) if invalid_entries else "None")

    print("\n🔍 Detailed Breakdown:")
    print("\nDistinction:")
    for name, mark in distinction:
        print(f"- {name}: {mark:.2f}")

    print("\nPass:")
    for name, mark in passed:
        print(f"- {name}: {mark:.2f}")

    print("\nFail:")
    for name, mark in failed:
        print(f"- {name}: {mark:.2f}")


#edit existing student record
def edit_student():
    roll = input("Enter roll number to edit: ").strip()
    filename = f"students/{roll}.json"

    if not os.path.exists(filename):
        print("❌ Student not found.")
        return

    with open(filename, "r") as file:
        student = json.load(file)

    print(f"\nCurrent info for {student['name']} (Roll: {student['roll']})")
    print("1. Edit Name")
    print("2. Edit Department")
    print("3. Edit Year")
    print("4. Edit/Add Semester Marks")
    print("5. Cancel")

    choice = input("Choose what to edit: ").strip()

    if choice == "1":
        new_name = input("Enter new name: ").strip()
        if new_name:
            student["name"] = new_name

    elif choice == "2":
        new_dept = input("Enter new department: ").strip()
        if new_dept:
            student["department"] = new_dept

    elif choice == "3":
        while True:
            new_year = input("Enter new year (1/2/3/4): ").strip()
            if new_year in {"1", "2", "3", "4"}:
                student["year"] = new_year
                break
            else:
                print("Invalid year.")

    elif choice == "4":
        while True:
            sem = input("Enter semester to edit (e.g., Semester 1): ").strip()
            if not sem:
                break

            if sem not in student["results"]:
                student["results"][sem] = {}

            while True:
                subject = input("Enter subject name (or Enter to finish): ").strip()
                if not subject:
                    break
                try:
                    marks = float(input(f"Enter marks for {subject}: ").strip())
                    if 0 <= marks <= 100:
                        student["results"][sem][subject] = marks
                    else:
                        print("❌ Marks must be between 0 and 100.")
                except ValueError:
                    print("❌ Invalid number.")

    elif choice == "5":
        print("Edit cancelled.")
        return
    else:
        print("Invalid option.")
        return

    with open(filename, "w") as file:
        json.dump(student, file, indent=4)

    print("✅ Student record updated successfully.")


# 🔸 Delete a student record
def delete_student():
    roll = input("Enter roll number to delete: ").strip()
    filename = f"students/{roll}.json"
    if not os.path.exists(filename):
        print("❌ Student record not found.")
        return
    confirm = input(f"Are you sure you want to delete the record for roll {roll}? (y/n): ").strip().lower()
    if confirm == "y":
        os.remove(filename)
        print(f"✅ Student record for roll {roll} deleted.")
    else:
        print("Deletion cancelled.")


# 🔸 Simple CLI Menu
if __name__ == "__main__":
    while True:
        print("\n📘 Student Record System")
        print("1. Add student")
        print("2. View student record")
        print("3. View grading summary")
        print("4. Edit student record")
        print("5. Delete student record")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            roll = input("Enter roll number: ")
            load_student(roll)
        elif choice == "3":
            save_grade_summary()
        elif choice == "4":
            edit_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("👋 Exiting the system. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")