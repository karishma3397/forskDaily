# -*- coding: utf-8 -*-
"""
Created on Wed May 23 10:32:32 2018

@author: KC
"""
from datetime import datetime
from pymongo import MongoClient
client = MongoClient('localhost',27017)
mydb = client.db_University

def add_Student(student_name,student_age,student_roll_no,student_branch):
    unique_student = mydb.students.find_one({"Student Roll No":student_roll_no})
    if unique_student:
        return "Student already exists"
    else:
        mydb.students.insert(
                {
                "Student Name" : student_name,
                "Student Age" : student_age,
                "Student Roll No" : student_roll_no,
                "Student Branch" : student_branch,
                "Date-Time" : datetime.now()
                }
                )
        return "Student added successfully"
def view_Student(student_roll_no):
    user = mydb.students.find_one({"Student Roll No": student_roll_no})
    if user:
        name = user["Student Name"]
        age = user["Student Age"]
        roll = user["Student Roll No"]
        branch = user["Student Branch"]
        time = user["Date-Time"]
        return {"'Student Name":name, "Student Age" : age, "Student Branch" : branch, "Student Roll No":roll }
    else:
        return "Sorry, No such user exists"
for i in range(0,10):    
    student_name = input("Enter Student Name:")
    student_age = input("Enter Student Age:")
    student_roll_no= input("Enter Student Roll No:")
    student_branch= input("Enter Student Branch:")
    print (add_Student(student_name,student_age,student_roll_no,student_branch))

user = input("Enter Student Roll No to find: ")
user_data = view_Student(user)

print (user_data)