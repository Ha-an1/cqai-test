from flask import Flask
import db_connect
from flask import jsonify

app=Flask(__name__)
@app.route('/')
def index():
    return "Welcome to the Employee Management System"

@app.route('/display',methods=['GET'])
def display():
    rows=db_connect.display_table()
    return jsonify(rows)

@app.route('/insert',methods=['POST'])
def insert():
    db_connect.insert_employee()
    return "Employee inserted successfully"

@app.route('/update',methods=['PUT'])
def update():
    db_connect.update_employee()
    return "Employee updated successfully"

@app.route('/delete',methods=['DELETE'])
def delete():
    db_connect.delete_employee()
    return "Employee deleted successfully"

if __name__ == '__main__':
    app.run(debug=True)