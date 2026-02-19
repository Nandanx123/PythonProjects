# Number Guessing Game

print("-----NUMBER GUESSING GAME-----")

secret_number = 49

attempt = 0
found = False

print("You have 10 attempts to guess a number!!")

while attempt < 10:
    guess = int(input("Guess the number : "))
    attempt += 1
    if guess > secret_number:
        print("High!")
        print("Attempts left :", 10 - attempt)
    elif guess < secret_number:
        print("Low!")
        print("Attempts left :", 10 - attempt)
    elif guess == secret_number:
        print("Correct")
        found = True
        print(f"You guessed the number in {attempt} attempts.")
        break

if not found:
    print("Game Over! The number was", secret_number)
