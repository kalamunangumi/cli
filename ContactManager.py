import re
import Contact
from datetime import datetime

class ContactBookManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        for contact in self.contacts:
            if contact.name == name:
                print("Contact already exists")
                return

        if not re.fullmatch(r"^\d{10}$",phone):
            print("Invalid phone number format")
            return

        if not re.match(pattern, email):
            print("Invalid email format")
            return
        
        new_contact = Contact.Contact(name, phone, email, created_at)
        self.contacts.append(new_contact)
        print("Contact added successfully.")
    
    def view_all(self):
        if not self.contacts:
            print("error: 404 No contacts found.")
            return
        
        for contact in self.contacts:
            print(contact)

    def search_by_name(self):
        name = input("Enter name to search ...")

        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(contact)
                return

        print("Contact not found.")

    def search_by_phone(self):
        phone = input("Enter phone number to search ...")

        for contact in self.contacts:
            if contact.phone == phone:
                print(contact)
                return

        print("Contact not found.")


    def search_by_email(self):
        email = input("Enter email to search ...")

        for contact in self.contacts:
            if contact.email.lower() == email.lower():
                print(contact)
                return

        print("Contact not found.")


    def search_by_date(self):
        date = input("Enter date to search ...")

        for contact in self.contacts:
            if contact.date == date:
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