# Student Result Management System

print("-----STUDENT RESULT SYSTEM-----")

# Create main menu

student = {}

while True:
    print("1: Add Student")
    print("2: View All Results")
    print("3: Show Topper")
    print("4: Show Class Statistics")
    print("5: Exit")

    choice = int(input("Enter your choice : "))

    if choice == 1:  # Add Student
        marks = []
        roll_number = int(input("Enter Roll No. : "))
        name = input("Enter Name : ")
        sub1_marks = int(input("Enter marks in subject 1 : "))
        sub2_marks = int(input("Enter marks in subject 2 : "))
        sub3_marks = int(input("Enter marks in subject 3 : "))

        marks.append(sub1_marks)
        marks.append(sub2_marks)
        marks.append(sub3_marks)

        total_marks = sub1_marks + sub2_marks + sub3_marks
        percentage = (total_marks / 300) * 100
        grade = None

        if percentage >= 90:
            grade = "A+"
        elif 75 <= percentage <= 89:
            grade = "A"
        elif 65 <= percentage <= 74:
            grade = "B"
        elif 55 <= percentage <= 64:
            grade = "C"
        else:
            grade = "Fail"

        student[roll_number] = {
            "name": name,
            "marks": marks,
            "total": total_marks,
            "percentage": percentage,
            "grade": grade
        }

        print("Student Added Successfully!")

    elif choice == 2:  # View All Results

        if len(student) == 0:
            print("No results yet!")
        else:
            print("----- STUDENT RESULTS-----")
            for roll, data in student.items():
                print(f"Roll Number : {roll}")
                print("Name :", student[roll]["name"])
                print("Marks :", student[roll]["marks"])
                print("Total :", student[roll]["total"])
                print("Percentage :", student[roll]["percentage"], end="%\n")
                print("Grade :", student[roll]["grade"])
                print("------------------------")

    elif choice == 3:  # Show Class Topper
        highest_percentage = 0
        topper_name = None
        topper_roll = None
        topper_grade = None
        for roll, data in student.items():
            percentage = data["percentage"]
            if percentage > highest_percentage:
                highest_percentage = percentage
                topper_roll = roll
                topper_name = data["name"]
                topper_grade = data["grade"]

        print("-----Class Topper-----")
        print("Name :", topper_name)
        print("Roll Number :", topper_roll)
        print("Percentage :", highest_percentage)
        print("Grade :", topper_grade)
        print("-----------------------")

    elif choice == 4:  # Show Class Statistics
        if len(student) == 0:
            print("No students added yet!")
        total_percentage = 0
        passed = 0
        failed = 0
        for roll, data in student.items():
            total_percentage += data["percentage"]
            if data["grade"] == "Fail":
                failed += 1
            else:
                passed += 1
        average_percentage = total_percentage / len(student)

        print("-----CLASS STATISTICS-----")
        print("Total Students :", len(student))
        print("Class Average :", average_percentage)
        print("Students Passed :", passed)
        print("Students Failed :", failed)
        print("--------------------------")

    elif choice == 5:  # Exit
        print("Thank you for using Student Result System!")
        print("GoodBye!")
        break
