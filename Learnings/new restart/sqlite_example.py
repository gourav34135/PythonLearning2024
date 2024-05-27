import sqlite3
import hashlib
from faker import Faker

# Create database and tables
def create_tables():
    conn = sqlite3.connect('office.db')
    c = conn.cursor()

    # Create employees table
    c.execute('''CREATE TABLE IF NOT EXISTS employees (
                 id INTEGER PRIMARY KEY,
                 first_name TEXT,
                 last_name TEXT,
                 city TEXT,
                 email TEXT,
                 phone TEXT,
                 sex TEXT,
                 salary REAL)''')

    # Create login table
    c.execute('''CREATE TABLE IF NOT EXISTS login (
                 id INTEGER PRIMARY KEY,
                 username TEXT UNIQUE,
                 password TEXT)''')

    conn.commit()
    conn.close()

# Signup user
def signup():
    conn = sqlite3.connect('office.db')
    c = conn.cursor()

    username = input("Enter username: ")
    password = input("Enter password: ")

    # Hash the password before storing it
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    c.execute("INSERT INTO login (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    conn.close()

# Login user
def login():
    conn = sqlite3.connect('office.db')
    c = conn.cursor()

    username = input("Enter username: ")
    password = input("Enter password: ")

    # Hash the password before

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    c.execute("SELECT * FROM login WHERE username=? AND password=?", (username, hashed_password))
    result = c.fetchone()

    conn.close()

    return result is not None

# Insert employee details manually
def insert_employee_details_manually():
    conn = sqlite3.connect('office.db')
    c = conn.cursor()

    num_employees = int(input("Enter the number of employees: "))

    for _ in range(num_employees):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        city = input("Enter city: ")
        email = input("Enter email: ")
        phone = input("Enter phone: ")
        sex = input("Enter sex: ")
        salary = float(input("Enter salary: "))

        c.execute("INSERT INTO employees (first_name, last_name, city, email, phone, sex, salary) VALUES (?, ?, ?, ?, ?, ?, ?)",
                  (first_name, last_name, city, email, phone, sex, salary))

    conn.commit()
    conn.close()

# Insert employee details using Faker
def insert_employee_details_faker():
    fake = Faker()

    conn = sqlite3.connect('office.db')
    c = conn.cursor()

    num_employees = int(input("Enter the number of employees to generate using Faker: "))

    for _ in range(num_employees):
        first_name = fake.first_name()
        last_name = fake.last_name()
        city = fake.city()
        email = fake.email()
        phone = fake.phone_number()
        sex = fake.random_element(elements=('Male', 'Female'))
        salary = fake.random_int(min=20000, max=100000)

        c.execute("INSERT INTO employees (first_name, last_name, city, email, phone, sex, salary) VALUES (?, ?, ?, ?, ?, ?, ?)",
                  (first_name, last_name, city, email, phone, sex, salary))

    conn.commit()
    conn.close()

# Search for employee details using any one of the employee details
def search_employee():
    conn = sqlite3.connect('office.db')
    c = conn.cursor()

    columns = ['first_name', 'last_name', 'city', 'email', 'phone', 'sex', 'salary']
    print("Choose the search term:")
    for i, column in enumerate(columns, 1):
        print(f"{i}. {column}")

    choice = int(input("Enter your choice: "))
    search_term = columns[choice - 1]
    search_value = input(f"Enter the {search_term} of the employee: ")

    c.execute(f"SELECT * FROM employees WHERE {search_term}=?", (search_value,))
    result = c.fetchall()

    if result:
        print("Employee details:")
        for row in result:
            print(row)
        return result[0]  # Return the first matching employee details
    else:
        print("No employee found with the specified detail.")
        return None

# Update employee details
def update_employee_details(employee_id):
    conn = sqlite3.connect('office.db')
    c = conn.cursor()

    print("\nChoose the detail you want to update:")
    print("1. First Name")
    print("2. Last Name")
    print("3. City")
    print("4. Email")
    print("5. Phone")
    print("6. Sex")
    print("7. Salary")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        new_value = input("Enter the new First Name: ")
        c.execute("UPDATE employees SET first_name=? WHERE id=?", (new_value, employee_id))
    elif choice == 2:
        new_value = input("Enter the new Last Name: ")
        c.execute("UPDATE employees SET last_name=? WHERE id=?", (new_value, employee_id))
    elif choice == 3:
        new_value = input("Enter the new City: ")
        c.execute("UPDATE employees SET city=? WHERE id=?", (new_value, employee_id))
    elif choice == 4:
        new_value = input("Enter the new Email: ")
        c.execute("UPDATE employees SET email=? WHERE id=?", (new_value, employee_id))
    elif choice == 5:
        new_value = input("Enter the new Phone: ")
        c.execute("UPDATE employees SET phone=? WHERE id=?", (new_value, employee_id))
    elif choice == 6:
        new_value = input("Enter the new Sex: ")
        c.execute("UPDATE employees SET sex=? WHERE id=?", (new_value, employee_id))
    elif choice == 7:
        new_value = float(input("Enter the new Salary: "))
        c.execute("UPDATE employees SET salary=? WHERE id=?", (new_value, employee_id))
    else:
        print("Invalid choice.")
        return

    conn.commit()
    conn.close()
    print("Employee details updated successfully!")

# Main function
def main():
    create_tables()

    print("Welcome to the Office Management System")

    while True:
        print("\n1. Sign Up")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            signup()
            print("User signed up successfully!")
        elif choice == '2':
            if login():
                print("Login successful!")

                # After successful login, ask user what action they want to take
                while True:
                    print("\nWhat would you like to do?")
                    print("1. Input Employee Details Manually")
                    print("2. Generate Employee Details using Faker")
                    print("3. Search for Employee Details")
                    print("4. Update Employee Details")
                    print("5. Logout")
                    action_choice = input("Enter your choice: ")

                    if action_choice == '1':
                        insert_employee_details_manually()
                        print("Employee details inserted successfully!")
                    elif action_choice == '2':
                        insert_employee_details_faker()
                        print("Employee details generated using Faker successfully!")
                    elif action_choice == '3':
                        search_result = search_employee()
                        if search_result:
                            print("Employee details found!")
                    elif action_choice == '4':
                        search_result = search_employee()
                        if search_result:
                            update_employee_details(search_result[0])  # Pass employee id for updating details
                    elif action_choice == '5':
                        print("Logging out.")
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == '3':
            print("Exiting program.")
             
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
