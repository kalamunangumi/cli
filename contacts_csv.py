import csv
import Contact

def save_contacts(contacts, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['name', 'phone', 'email', 'created_at']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for contact in contacts:
            writer.writerow({
                'name': contact.name,
                'phone': contact.phone,
                'email': contact.email,
                'created_at': contact.created_at
            })

def load_contacts(filename):
    contacts = []
    try:
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                contact = Contact.Contact(
                    name=row['name'],
                    phone=row['phone'],
                    email=row['email'],
                    created_at=row['created_at']
                )
                contacts.append(contact)
    except FileNotFoundError:
        print("No existing contacts found. Starting with an empty contact list.")
    return contacts

    