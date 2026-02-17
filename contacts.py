import re
contacts = []
def valid_name(name):
    return name.isalpha()
def valid_phone(phone):
    return phone.isdigit() and len(phone) == 10
def valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)
def valid_address(address):
    return address.replace(" ", "").isalpha()
def add_contact():
    name = input("Enter Name: ")
    if not valid_name(name):
        print("Invalid name! Letters only.")
        return
    phone = input("Enter Phone: ")
    if not valid_phone(phone):
        print("Invalid phone! Must be 10 digits.")
        return
    email = input("Enter Email: ")
    if not valid_email(email):
        print("Invalid email format.")
        return
    address = input("Enter Address: ")
    if not valid_address(address):
        print("Invalid address! Letters only.")
        return
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print("Contact added successfully!")
def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    print("\nContact List:")
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['name']} - {c['phone']}")
def search_contact():
    keyword = input("Enter name or phone to search: ").lower()
    found = False
    for c in contacts:
        if keyword in c["name"].lower() or keyword in c["phone"]:
            print("\nContact Found:")
            for key, value in c.items():
                print(key.capitalize(), ":", value)
            found = True
    if not found:
        print("Contact not found.")
def update_contact():
    name = input("Enter name to update: ").lower()
    for c in contacts:
        if c["name"].lower() == name:
            phone = input("New phone: ")
            if not valid_phone(phone):
                print("Invalid phone!")
                return
            email = input("New email: ")
            if not valid_email(email):
                print("Invalid email!")
                return
            address = input("New address: ")
            if not valid_address(address):
                print("Invalid address!")
                return
            c["phone"] = phone
            c["email"] = email
            c["address"] = address
            print("Contact updated!")
            return
    print("Contact not found.")
def delete_contact():
    name = input("Enter name to delete: ").lower()
    for c in contacts:
        if c["name"].lower() == name:
            contacts.remove(c)
            print("Contact deleted!")
            return
    print("Contact not found.")
while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = input("Choose option: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting Contact Book...")
        break
    else:
        print("Invalid choice!")
