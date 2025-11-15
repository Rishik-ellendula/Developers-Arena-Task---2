print("===============================================")
print("            STUDENT GRADE CALCULATOR           ")
print("===============================================\n")

students = []

def classify_grade(marks):
    """Return grade & comment based on score."""
    if marks >= 90:
        return "A", "Outstanding performance! 🌟"
    elif marks >= 75:
        return "B", "Great job! Keep improving 👍"
    elif marks >= 60:
        return "C", "Good effort! Needs consistency 🙂"
    elif marks >= 40:
        return "D", "Below average. Study harder."
    else:
        return "F", "Failed. Additional effort required ❗"


def add_student():
    """Take user input & add a student record."""
    print("\n------ Add Student Marks ------")

    name = input("Enter student name: ").strip().title()

    try:
        marks = float(input("Enter marks (0-100): "))
        if marks < 0 or marks > 100:
            print("❗ Marks must be between 0 and 100. Setting to 0.")
            marks = 0
    except:
        print("❗ Invalid marks! Setting to 0.")
        marks = 0

    grade, comment = classify_grade(marks)

    students.append([name, marks, grade, comment])

    print("\n✅ Student Added Successfully!")
    print("-----------------------------------")
    print(f"Name    : {name}")
    print(f"Marks   : {marks}")
    print(f"Grade   : {grade}")
    print(f"Remark  : {comment}")
    print("-----------------------------------")


def view_all_students():
    """Display all students and their grades."""
    print("\n===============================================")
    print("               ALL STUDENT RESULTS              ")
    print("===============================================")

    if not students:
        print("No student records found.")
        return

    for s in students:
        print(f"\nName   : {s[0]}")
        print(f"Marks  : {s[1]}")
        print(f"Grade  : {s[2]}")
        print(f"Remark : {s[3]}")
        print("----------------------------------------------")


def class_summary():
    """Show highest, lowest, and average marks."""
    print("\n=============== CLASS SUMMARY ===============")

    if not students:
        print("No data available!")
        return

    marks_list = [s[1] for s in students]
    
    highest = max(marks_list)
    lowest = min(marks_list)
    avg = sum(marks_list) / len(marks_list)

    toppers = [s[0] for s in students if s[1] == highest]
    low_scorers = [s[0] for s in students if s[1] == lowest]

    print(f"Highest Marks : {highest}  ({', '.join(toppers)})")
    print(f"Lowest Marks  : {lowest}  ({', '.join(low_scorers)})")
    print(f"Class Average : {round(avg, 2)}")
    print("=============================================")

while True:

    print("\n=========== MAIN MENU ===========")
    print("1. Add Student")
    print("2. View All Students")
    print("3. View Class Summary")
    print("4. Exit")
    print("=================================")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_all_students()
    elif choice == "3":
        class_summary()
    elif choice == "4":
        print("\nThank you for using the Grade Calculator! 🎉")
        break
    else:
        print("❗ Invalid choice! Please select 1-4.")
