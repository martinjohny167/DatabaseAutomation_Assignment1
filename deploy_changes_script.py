import mysql.connector

# Database connection details
db_config = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
    'database': 'your_database'
}

# SQL command to add a new table
sql_command = """
CREATE TABLE IF NOT EXISTS new_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

# Connect to the database and execute the command
try:
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    cursor.execute(sql_command)
    connection.commit()

    print("Table created successfully.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()