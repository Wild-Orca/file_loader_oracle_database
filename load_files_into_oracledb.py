# Import necessary libraries
import os
import cx_Oracle

# Initialize Oracle Client with the specified directory for the Oracle Instant Client
cx_Oracle.init_oracle_client(lib_dir=r"client_path") # Example: C:\Users\godmn\Documents\instantclient-basic-windows.x64-21.12.0.0.0dbru\instantclient_21_12

# Oracle Database connection details
db_user = 'db_user'
db_password = 'db_password.'
db_dsn = 'hostname_or_ip:port_number/service_name_or_sid'

# Function to read file content based on the file type
def read_file_content(file_path, is_text_file):
    with open(file_path, 'r' if is_text_file else 'rb') as file:
        return file.read()

try:
    # Attempt to connect to the Oracle database
    # To specify privilege level, use mode=cx_Oracle.SYSDBA (or any other role)
    connection = cx_Oracle.connect(db_user, db_password, db_dsn, mode=cx_Oracle.SYSDBA)
    cursor = connection.cursor()

    # Path to the folder containing files to be inserted into the Oracle database
    folder_path = r'folder_path'

    print(folder_path)

    # Iterate over files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Extract file name without extension and file extension
        file_name_without_extension, file_extension = os.path.splitext(filename)
        file_extension = file_extension.lower()
        
        # Check if the file is a text file based on the extension
        is_text_file = file_extension.endswith(('.txt', '.log', '.sql', '.pl', '.xml'))

        # Read file content based on the file type
        if is_text_file:
            file_content_clob = read_file_content(file_path, is_text_file)
            file_content_blob = None
        else:
            file_content_blob = read_file_content(file_path, is_text_file)
            file_content_clob = None

        # Insert data into the Oracle table
        cursor.execute("INSERT INTO tb_test (file_name, file_extension, file_content_blob, file_content_clob) VALUES (:1, :2, :3, :4)",
                       (file_name_without_extension, file_extension, file_content_blob, file_content_clob))

except cx_Oracle.Error as e:
    # Handle any potential errors during connection or insertion
    print("Error:", e)

finally:
    # Commit changes to the database
    connection.commit()
    print("Files inserted successfully.")
    # Close the cursor and connection in the finally block to ensure they are closed even if an exception occurs
    if 'cursor' in locals() and cursor is not None:
        cursor.close()
    if 'connection' in locals() and connection is not None:
        connection.close()