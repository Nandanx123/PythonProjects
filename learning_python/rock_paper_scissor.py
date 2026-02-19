import random

print("-----ROCK PAPER SCISSOR GAME-----")

choices = ['rock', 'paper', 'scissor']
user_score = 0
computer_score = 0

while True:
    user_choice = input("Enter rock or paper or scissor : ").lower().strip()
    if user_choice not in choices:
        print("Invalid Choice! Try Again..")

    computer_choice = random.choice(choices)
    print("Computer chose :", computer_choice)

    if user_choice == computer_choice:
        print("It's a draw!")
    elif user_choice == 'rock' and computer_choice == 'scissor':
        print("User won!")
        user_score += 1
    elif user_choice == 'scissor' and computer_choice == 'paper':
        print("User won!")
        user_score += 1
    elif user_choice == 'paper' and computer_choice == 'rock':
        print("User won!")
        user_score += 1
    else:
        print("Computer won!")
        computer_score += 1

    play_again = input("Do you want to play again (Y / N) : ")

    if play_again == 'Y'.strip() or play_again == 'y'.strip():
        continue
    elif play_again == 'N'.strip() or play_again == 'n'.strip():
        break
    print("-" * 25)

print("User score :", user_score)
print("Computer score :", computer_score)

if user_score > computer_score:
    print("User won most games!")
elif user_score == computer_score:
    print("It's draw")
else:
    print("Computer won most games!")
