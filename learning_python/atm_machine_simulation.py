# ATM Machine Simulation

print("-----ATM MACHINE SIMULATION-----")

pin = 12345
balance = 10000
login_attempts = 0

correct_pin = False
while login_attempts < 3:
    pin_no = int(input("Enter pin : "))

    if pin_no != pin:
        login_attempts += 1
    else:
        correct_pin = True
        while True:
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = int(input("Choose an option : "))

            if choice == 1:
                print("Current Balance :", balance)

            elif choice == 2:
                dep_amt = int(input("Enter the amount to deposit : "))
                balance += dep_amt
                print("Updated Balance :", balance)

            elif choice == 3:
                withdraw_amt = int(input("Enter the amount to withdraw : "))
                if withdraw_amt <= balance:
                    balance -= withdraw_amt
                    print("Updated Balance : ", balance)
                else:
                    print("Insufficient Balance!")

            elif choice == 4:
                print("Thank You for using ATM!")
                login_attempts = 3
                break

if not correct_pin:
    print("Account Locked")
