#Personal Expense Tracker

#Welcome Message
print("Welcome to Personal Expense Tracker :-")
print()

#Taking User Details
name = input("Enter your name : ")
name.strip()
name.capitalize()
budget = float(input("Enter monthly budget : "))

print(f"Hello {name}, Your monthly budget is {budget}")
print()

#Creating Expense Categories
categories = ("Food", "Transport", "Entertainment", "Bills", "Other")
print("Available Expense Categories :-")
print(f"1 : {categories[0]}")
print(f"2 : {categories[1]}")
print(f"3 : {categories[2]}")
print(f"4 : {categories[3]}")
print(f"5 : {categories[4]}")
print()

#Initializing Data Storage
expenses = []
used_categories = set()

#Show Menu

while(True):
    print("Choose an option :-")
    print("1. Add Expense")
    print("2. View all Expenses")
    print("3. View Summary")
    print("4. Exit")

    choice = int(input("Enter your choice : "))
    if choice == 1:
        exp_amt = float(input("Enter expense amount : "))
        exp_cat = input("Enter category : ")
        exp_desc = input("Enter description : ")
        tup = (exp_amt,exp_cat, exp_desc)
        expenses.append(tup)
        used_categories.add(exp_cat)
    elif choice == 2:
        print("Your Expenses :-")
        for i in expenses:
            exp_amt, exp_cat,exp_desc = i
            print(f"1. Amount: {exp_amt} | Category : {exp_cat} | Description : {exp_desc}")
    elif choice == 3:
        print("Expense Summary :-")
        total_spent = 0
        for i in expenses:
            exp_amt, exp_cat, exp_desc = i
            total_spent += exp_amt
        remaining_budget = budget - total_spent
        print("Total spent :", total_spent)
        print("Remaining budget :", remaining_budget)
        if total_spent <= budget:
            print("Budget Status : Within Budget")
        else:
            print("Budget Status : Budget Exceeded")
        print("Categories used", used_categories)
    elif choice == 4:
        print("Thank You for using Personal Expense Tracker!")
        print("GoodBye!!")
        break
