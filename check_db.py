import sqlite3

# Connect to the database
conn = sqlite3.connect('form_data.db')
cursor = conn.cursor()

# Execute a query to view data (e.g., all rows from a table)
cursor.execute("SELECT * FROM user_data")
data = cursor.fetchall()

# Display the data
for row in data:
    print(row)

# Close the database connection
conn.close()
