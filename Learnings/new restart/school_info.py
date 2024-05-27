import sqlite3

def create_database():
    conn = sqlite3.connect('school.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS student_info (
                    id INTEGER PRIMARY KEY,
                    firstname TEXT,
                    lastname TEXT,
                    fathers_name TEXT,
                    dob TEXT,
                    city TEXT,
                    contact_no TEXT
                )''')

    c.execute('''CREATE TABLE IF NOT EXISTS student_bank (
                    id INTEGER PRIMARY KEY,
                    firstname TEXT,
                    lastname TEXT,
                    account_number TEXT,
                    ifsc_code TEXT,
                    city TEXT
                )''')

    conn.commit()
    conn.close()


def insert_student_info():
    firstname = input("Enter first name: ")
    lastname = input("Enter last name: ")
    fathers_name = input("Enter father's name: ")
    dob = input("Enter date of birth (YYYY-MM-DD): ")
    city = input("Enter city: ")
    contact_no = input("Enter contact number: ")

    conn = sqlite3.connect('school.db')
    c = conn.cursor()
    c.execute('''INSERT INTO student_info (firstname, lastname, fathers_name, dob, city, contact_no) 
                VALUES (?, ?, ?, ?, ?, ?)''', (firstname, lastname, fathers_name, dob, city, contact_no))
    conn.commit()
    conn.close()


def insert_student_bank():
    firstname = input("Enter first name: ")
    lastname = input("Enter last name: ")
    account_number = input("Enter account number: ")
    ifsc_code = input("Enter IFSC code: ")
    city = input("Enter city: ")

    conn = sqlite3.connect('school.db')
    c = conn.cursor()
    c.execute('''INSERT INTO student_bank (firstname, lastname, account_number, ifsc_code, city) 
                VALUES (?, ?, ?, ?, ?)''', (firstname, lastname, account_number, ifsc_code, city))
    conn.commit()
    conn.close()

def main():
    create_database()

    while True:
        print("\nChoose table to insert data:")
        print("1. Student Info")
        print("2. Student Bank")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            insert_student_info()
        elif choice == '2':
            insert_student_bank()
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
