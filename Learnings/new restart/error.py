import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import mysql.connector

# Sample data
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 22],
        'Salary': [50000, 60000, 45000]}

# Create a DataFrame using pandas
df = pd.DataFrame(data)

# Display DataFrame
print("Original DataFrame:")
print(df)

# Add 10% bonus to Salary using numpy
df['Salary'] = np.round(df['Salary'] * 1.1, 2)

# Display updated DataFrame
print("\nDataFrame with Bonus:")
print(df)

# Plot Age vs Salary using matplotlib
plt.scatter(df['Age'], df['Salary'])
plt.xlabel('Age')
plt.ylabel('Salary')
plt.title('Age vs Salary')
plt.show()

# Get current date using datetime
current_date = datetime.datetime.now()
print("\nCurrent Date:", current_date)

# Connect to MySQL database
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="systum",
        database="crime"
    )

    if connection.is_connected():
        cursor = connection.cursor()
        # Example query
        query = "SELECT * FROM your_table"
        cursor.execute(query)
        result = cursor.fetchall()
        print("\nMySQL Query Result:")
        for row in result:
            print(row)

except mysql.connector.Error as e:
    print("Error connecting to MySQL:", e)
