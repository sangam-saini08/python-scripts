import csv
import os

FILE_NAME = "contact.csv"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME,'w',newline="",encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name","Phone","Email"])

def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    
    with open(FILE_NAME,"r",encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Name'].lower() == name.lower():
                print("Contact is Already exits: ")
                return
            
    with open(FILE_NAME,'a',encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name,phone,email])
        print("Contact added")

def view_contacts():
    print("List of Contacts!")
    with open(FILE_NAME,"r",encoding="utf-8") as f:
        contacts = list(csv.reader(f))
        for row in contacts:
            if row:
                print(f"{row[0]} | {row[1]} | {row[2]}")
                
        return

def search():
    name = input("Enter Name to Search: ").strip()
    with open(FILE_NAME,"r",encoding="utf-8") as f:
        rows = csv.DictReader(f)
        for row in rows:
            if row["Name"].lower() == name.lower():
                print(f"Result: {row['Name']} | {row['Phone']} | {row['Email']}")
                return
            
def delete_contact():
    name = input("Enter Name to Delete: ").strip()
    delet_index = -1
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        rows = list(csv.reader(f))

    # Find and remove the row
    for index, row in enumerate(rows):
        if row and row[0].strip().lower() == name.lower():
            delet_index = index
            break

    if delet_index == -1:
        print("❌ Contact not found.")
        return

    rows.pop(delet_index)

    with open(FILE_NAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)  # ✅ Write rows properly

    print("✅ Contact deleted successfully.")
        


    with open(FILE_NAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)  # ✅ Write rows properly

    print("✅ Contact deleted successfully.")


def main():
    print("\n-- Welcome to Phone Book --\n")
    while True:
        print("\n1. Add Contacts")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. delete Contact")
        print("5. exit\n")

        choice = input("Enter the Choice: ")

        match choice:
            case "1":
                add_contact()
            case "2":
                view_contacts()
            case "3":
                search()
            case "4":
                delete_contact()
            case "5":
                break                


if __name__ == "__main__":
    main()        
