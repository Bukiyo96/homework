import json
import os
import datetime
from datetime import datetime

register = []
student = {}
# Read data from user
st_num = int(input("How Many Students do you want to add? "))
sub_num = int(input("How many Subjects they have? "))

# For cycle
for j in range(0, st_num):
    # Read names
    s_name = input("Name: ")
    student.update({"Name": s_name})
    suma = 0
    for i in range(0, sub_num):
        # Read data about subj and mark
        subject = input("Subject: ")
        mark = float(input("Mark: "))

        # Add this data to dictionary
        student.update({subject: mark})
        suma += mark
        #
    media = suma / sub_num
    student.update({"Media": media})

    curDT = datetime.now()
    date_time = curDT.strftime("%m/%d/%Y, %H:%M:%S")

    student.update({"Timestamp": date_time})
    # Add students to register

    register.append(student.copy())

to_json = json.dumps(register)

while True:
    print("Doresti sa deschizi fisierul json creat?: ")
    print("1. Da")
    print("2. Nu")

    alegerea = int(input())
    if alegerea == 1:
        with open("sample.json", "w") as outfile:
         outfile.write(to_json)
         print(to_json)
        break
    if alegerea == 2:
        print("inchiderea programului")
        break

