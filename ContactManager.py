class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    
    def __str__(self):
        return f"Name: {self.name} Phone: {self.phone} Email: {self.email}"

class ContactBookManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")

        for contact in self.contacts:
            if contact.name == name:
                print("Contact already exists")
                return
        
        new_contact = Contact(name, phone, email)
        self.contacts.append(new_contact)
        print("Contact added successfully.")
    
    def view_all(self):
        if not self.contacts:
            print("No contacts found.")
            return
        
        for contact in self.contacts:
            print(contact)

    def search_contact(self):
        name = input("Enter name to search ...")

        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(contact)
                return

        print("Contact not found.")

    def delete_contact(self, contact):
        name = input("Enter name to delete: ")

        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)

        print("Contact not found.")

    def update_contact(self):
        name = input("Enter contact to update: ")
        
        for contact in self.contacts:
            if contact.name.loweer() == name.lower():
                contact.phone = input("Enter new phone: ")
                contact.email = input("Enter new email: ")
                return

        print("Contact not found.")
    
def main():
    manager = ContactBookManager()

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
