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

def display_table():
    cursor.execute('SELECT * FROM employees')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    return rows
        
def insert_employee():
    id= input("Enter employee ID: ")
    name = input("Enter employee name: ")
    department=input("Enter employee department: ")
    salary=input("Enter employee salary:")
    cursor.execute('INSERT INTO employees (id, name, department, salary) VALUES (%s, %s, %s, %s)', (id, name, department, salary))
    connection.commit()    
    connection.close()

def update_employee():
    print("Enter employee ID to update salary: ")
    id = input("Enter employee ID: ")
    salary= input("Enter new salary: ")
    cursor.execute('UPDATE employees SET salary = %s WHERE id =%s',(salary,id))
    connection.commit()
    connection.close()
    
def delete_employee():
    print("Enter employee ID to delete: ")
    id = input("Enter employee ID: ")
    cursor.execute('DELETE FROM employees WHERE id = %s', (id,))
    connection.commit()
    connection.close()

