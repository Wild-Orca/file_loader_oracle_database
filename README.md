<strong>File Loader for Oracle Database</strong>

This Python script is designed to read files from a specified folder and load them into an Oracle Database table. It utilizes the cx_Oracle library for Oracle Database connectivity.
<br><hr><br><strong>Prerequisites</strong>

    Install Oracle Instant Client:
        Follow the instructions in the official Oracle documentation to install Oracle Instant Client: Oracle Instant Client Installation
        Unzip the downloaded package into the desired folder.

    Configure Oracle Instant Client Path:
        Open the Python script load_files_into_oracledb.py.
        Locate and update line 6 with the correct path to the Oracle Instant Client directory.
        
    Example: C:\Users\godmn\Documents\instantclient-basic-windows.x64-21.12.0.0.0dbru\instantclient_21_12

<strong>Install cx_Oracle Library:</strong>

    Install the cx_Oracle library using the following command:

        pip install cx_Oracle

<strong>Usage</strong>

    Run the Script:
        After completing the prerequisites, run the Python script load_files_into_oracledb.py.
        The script will connect to the Oracle Database, read files from the specified folder, and insert them into the designated table.

    Configure Database Connection:
        Open the script and update the following database connection details:
            db_user: Your Oracle Database username.
            db_password: Your Oracle Database password.
            db_dsn: Your Oracle Database connection details (hostname_or_ip:port_number/service_name_or_sid).

    Customize Table and Column Names:
        Modify the script to match your Oracle Database table structure, including column names and types.
        Update the SQL statement in the script accordingly.

<strong>Notes</strong>

    Ensure that Oracle Instant Client is properly installed, and the path is correctly configured.
    The cx_Oracle library must be installed using the provided command.
    Customize the script with your Oracle Database connection details and table structure.

By following these steps, you should be able to use the script to load files into your Oracle Database table seamlessly. If you encounter any issues, refer to the documentation or seek assistance from the Oracle community.
