class Contact:
    def __init__(self, name, phone, email, created_at):
        self.name = name
        self.phone = phone
        self.email = email
        self.created_at = created_at
    
    def __str__(self):
        return f"Name: {self.name} Phone: {self.phone} Email: {self.email} Created At: {self.created_at}"
