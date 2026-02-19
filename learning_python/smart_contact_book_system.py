# Smart Contact Book System

print("-----CONTACT BOOK-----")

# Create Menu

contacts = {}

while True:
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Total Contacts")
    print("7. Exit")

    print("-" * 22)

    choice = int(input("Enter choice : "))

    if choice == 1:  # Add Contact
        name = input("Enter name : ").strip().lower()
        if name in contacts:
            print("Contact already exists!")
        else:
            phone_no = input("Enter phone number : ")
            email = input("Enter email : ")
            if email.endswith("@gmail.com"):
                city = input("Enter city : ").capitalize()

                contacts[name] = {
                    "phone_no": phone_no,
                    "email": email,
                    "city": city,
                }
                print("Contact Added Successfully!")
            else:
                print("Email should end with @gmail.com")
        print("-" * 22)

    elif choice == 2:  # View all Contacts
        if len(contacts) == 0:
            print("No contacts found!")
        else:
            print("-----All Contacts-----")
            for name, data in contacts.items():
                print("Name :", name.capitalize())
                print("Phone No. :", data["phone_no"])
                print("Email :", data["email"])
                print("City :", data["city"])
                print("-" * 22)

    elif choice == 3:  # Search contacts
        search_name = input("Enter name to search : ").strip().lower()
        if search_name in contacts:
            print("Phone Number :", contacts[search_name]["phone_no"])
            print("Email :", contacts[search_name]["email"])
            print("City :", contacts[search_name]["city"])
        else:
            print("Contact not found!")
        print("-" * 22)

    elif choice == 4:  # Update contacts
        update_name = input("Enter name : ").strip().lower()

        if update_name in contacts:
            print("1. Phone Number")
            print("2. Email")
            print("3. City")

            update_choice = int(input("Choose Field : "))

            if update_choice == 1:
                contacts[update_name]["phone_no"] = input("Enter new Phone number : ")
            elif update_choice == 2:
                contacts[update_name]["email"] = input("Enter new Email : ")
            elif update_choice == 3:
                contacts[update_name]["city"] = input("Enter new City : ")

            print("Contact Updated Successfully!")
        else:
            print("Contact Not Found!")
        print("-" * 22)

    elif choice == 5:  # Delete contact
        delete_name = input("Enter name : ").strip().lower()
        if delete_name in contacts:
            del contacts[delete_name]
            print("Contact deleted successfully!")
        else:
            print("No contact found with that name!")
        print("-" * 22)

    elif choice == 6:  # Show total contacts
        print("Total contacts :", len(contacts))
        print("-" * 22)

    elif choice == 7:  # Exit
        print("Exiting....")
        print("Thank you for using contact book!")
        break
