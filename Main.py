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
            manager.search_contact()
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