import os
import datetime
import mysql.connector
from mysql.connector import Error

# Database connection details
db_config = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
    'database': 'your_database'
}

# Backup directory
backup_dir = '/path/to/backup/directory'

# Create a unique filename using timestamp
timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
backup_file = os.path.join(backup_dir, f'db_backup_{timestamp}.sql')

# Backup command using mysqldump
backup_command = (
    f"mysqldump -u {db_config['user']} -p{db_config['password']} "
    f"{db_config['database']} > {backup_file}"
)

# Function to execute the backup
def perform_backup():
    try:
        # Check if the backup directory exists, create it if not
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
            print(f"Created backup directory: {backup_dir}")

        # Execute the backup command
        return_code = os.system(backup_command)

        # Check if the backup was successful
        if return_code == 0:
            print(f"Backup completed successfully: {backup_file}")
        else:
            raise Exception(f"Backup command failed with return code: {return_code}")

    except Exception as e:
        print(f"Backup failed: {e}")
        # Optionally, log the error to a file or send a notification
        # Example: log_error_to_file(e)

# Main execution
if __name__ == "__main__":
    perform_backup()