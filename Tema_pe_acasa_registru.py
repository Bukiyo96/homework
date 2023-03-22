


registru = []
registru1 = []
registru2 = []
registru3 = []
student = {}
student1 = {}
student2 = {}
student3 = {}


nr_studenti = int(input("Cati studenti doresti sa adaugi?:"))
nr_obiecte = int(input("Cate obiecte doresti sa adaugi?:"))


for s in range(0, nr_studenti):
    nume_student =input("Nume ")
    student.update({"Name " : nume_student})

    for o in range(0, nr_obiecte):
        obiect = input("Obiect ")
        nota = int(input("Nota "))

        student.update({obiect: nota})

    registru.append(student)


for s in range(0, nr_studenti):
    nume_student =input("Nume ")
    student1.update({"Name " : nume_student})

    for o in range(0, nr_obiecte):
        obiect = input("Obiect ")
        nota = int(input("Nota "))

        student1.update({obiect: nota})

    registru1.append(student1)

for s in range(0, nr_studenti):
     nume_student = input("Nume ")
     student2.update({"Name ": nume_student})

     for o in range(0, nr_obiecte):
        obiect = input("Obiect ")
        nota = int(input("Nota "))

        student2.update({obiect: nota})

     registru2.append(student2)

for s in range(0, nr_studenti):
    nume_student =input("Nume ")
    student3.update({"Name " : nume_student})

    for o in range(0, nr_obiecte):
        obiect = input("Obiect ")
        nota = int(input("Nota "))

        student3.update({obiect: nota})

    registru3.append(student3)

print(registru)
print(registru1)
print(registru2)
print(registru3)

