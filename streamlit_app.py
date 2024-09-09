import streamlit as st
import pyodbc 

SERVER = '<SQLEXPRESS>'
DATABASE_NAME = '<Music_01>'
USERNAME = '<TOSHIBA>'
PASSWORD = '<Tereliye>'

connectionString = f'DRIVER= {{SQL Server}}; SERVER = SERVER; DATABASE = DATABASE_NAME; USERNAME = USERNAME; PASSWORD = PASSWORD;'

conn = pyodbc.connect(connectionString)

SQL_QUERY="""SELECT * FROM ALBUM"""

cursor = conn.cursor()
cursor.execute(SQL_QUERY)

records = cursor.fetchall()
for r in records:
    print(r)
