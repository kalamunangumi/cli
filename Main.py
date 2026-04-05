import ContactManager

def main():
    manager = ContactManager.ContactBookManager()

    while True:
        print("*******Select the task that you want to perform*******")
        print("1: Add contact")
        print("2: View all")
        print("3: Search")
        print("4: Delete")
        print("5: Update contact")
        print("6: Exit")
    
        choice = input("")
 
        if choice == "1":
            manager.add_contact()
        elif choice == "2":
            manager.view_all()
        elif choice == "3":
            print("1: Search contact by name")
            print("2: Search contact by phone")
            print("3: Search contact by email")
            print("4: Search contact by created date")
            search_choice = input("Select search criteria: ")
            if search_choice == '1':
                manager.search_by_name()
            elif search_choice == '2':
                manager.search_by_phone()
            elif search_choice == '3':
                manager.search_by_email()
            elif search_choice == '4':
                manager.search_by_date()
            else:
                print("Invalid choice")
        elif choice == "4":
            manager.delete_contact()
        elif choice == "5":
            manager.update_contact()
        elif choice == "6":
            print("William was here ...")
            break
        else:
            print("Invalid choice")

main()