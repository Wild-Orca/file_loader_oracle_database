A Python script to read an OS folder and load the files into a Oracle Database Table

First, install Oracle Instant Client by following this link<br>
https://docs.oracle.com/cd/E83411_01/OREAD/installing-oracle-database-instant-client.htm

Then, unzip it into the desired folder, and change load_files_into_oracledb.py line 6 with the correct path<br> 
Example: C:\Users\godmn\Documents\instantclient-basic-windows.x64-21.12.0.0.0dbru\instantclient_21_12

For cx_Oracle to work, its necessary to install it by typing: <br>
pip install cx_Oracle 
