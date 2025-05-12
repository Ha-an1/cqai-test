from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()  

connection = mysql.connector.connect(
    host=os.getenv('DB_HOST'),        
    user=os.getenv('DB_USER'),
    port=os.getenv('DB_PORT'),    
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_NAME')    
)

cursor = connection.cursor()

cursor.execute('SELECT * FROM employees')
rows = cursor.fetchall()
for row in rows:
    print(row)

connection.close()