
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
    # Add students to register

    register.append(student.copy())
#Print register
print(register)













