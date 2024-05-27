import sqlite3


conn = sqlite3.connect('example.db')


cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                  (id INTEGER PRIMARY KEY, name TEXT, position TEXT, salary REAL)''')
conn.commit()


cursor.execute("INSERT INTO employees (name, position, salary) VALUES (?, ?, ?)", ('John Doe', 'Software Engineer', 80000))
conn.commit()


cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()

for row in rows:
    print(row)


cursor.execute("UPDATE employees SET salary = ? WHERE id = ?", (90000, 1))
conn.commit()

cursor.execute("DELETE FROM employees WHERE id = ?", (1,))
conn.commit()

# Step 9: Close the connection when you're done
conn.close()
