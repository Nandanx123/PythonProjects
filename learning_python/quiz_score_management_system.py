# Smart Quiz System

# Print Welcome Message
print("-" * 35)
print("-: SMART QUIZ SYSTEM :-")
print("-" * 35)

# Creating Data Structures
quiz_questions = {
    1: ("Which is the capital of India?", "New Delhi", "Geography"),
    2: ("What's 12 squared?", "144", "Maths"),
    3: ("What gas do plants absorb from atmosphere?", "Carbon dioxide", "Science"),
    4: ("What does CPU stand for?", "Central Processing Unit", "Computer Science"),
    5: ("Which is the capital of Karnataka?", "Bengaluru", "Geography")
}
score_history = []

# Create infinite menu loop
while True:
    print("1. Start Quiz")
    print("2. View Score History")
    print("3. View Performance Summary")
    print("4. Exit")

    choice = int(input("Enter your choice : "))

    if choice == 1:  # Start Quiz
        score = 0
        topics_attempted = set()
        total_questions = len(quiz_questions)

        for number, data in quiz_questions.items():
            question_text = data[0]
            correct_answer = data[1]
            topic = data[2]

            print(f"Question {number} : {question_text}")
            user_answer = input("Your answer : ").strip()

            if user_answer.lower().strip() == correct_answer.lower().strip():
                print("Correct!")
                score += 1
            else:
                print("Wrong! Correct answer is : ", correct_answer)
            print("Topic", topic)

        percentage = (score / total_questions) * 100
        grade = None

        if percentage >= 90:
            grade = "A+"
        elif 75 <= percentage <= 89:
            grade = "A"
        elif 55 <= percentage <= 74:
            grade = "B"
        elif 35 <= percentage <= 54:
            grade = "C"
        else:
            grade = "FAIL"

        score_history.append(int(percentage))
        print("-----------------------")
        print("Quiz Completed!")
        print(f"Your score : {score} / {total_questions}")
        print(f"Percentage : {percentage}%")
        print(f"Grade : {grade}")
        print("-----------------------")

    elif choice == 2:  # View Score history

        print("-----Score History-----")
        if len(score_history) == 0:
            print("No attempts yet.")
        else:
            i = 0
            while i < len(score_history):
                print(f"Attempt {i + 1} : {score_history[i]}%")
                i += 1
        print("-----------------------")

    elif choice == 3:  # Performance summary
        if len(score_history) == 0:
            print("No score history!")
        else:
            highest_score = max(score_history)
            lowest_score = min(score_history)
            average_score = sum(score_history) / len(score_history)
            print("----Performance Summary----")
            print("Highest score :", highest_score)
            print("Lowest score :", lowest_score)
            print("Average score :", average_score)
            print("---------------------------")

    elif choice == 4:  # Exit
        print("Thank you for using Smart Quiz System!")
        print("GoodBye!")
        break
