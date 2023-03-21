



registru = [] #registru
registru1 = []
registru2 = []
registru3 = []
elev_materie = {} #elevi - materie
elev_materie1 = {}
elev_materie2 = {}
elev_materie3 = {}
note = {}
note1 = {}
note2 = {}
note3 = {}
m = ()

d = int(input("cati elevi vreai sa adaugi:? "))
e = int(input("cate materii vreai sa adaugi:? "))
f = int(input("cate note adaugi:? "))

for a1 in range(0,d):
    numestudenti = input("Numele ")
    elev_materie.update({"Nume": numestudenti})

    for a2 in range(0,e):
        obiect = input("Materie ")
        elev_materie.update({"Materie ": obiect })

        for a3 in range(0,f):
            nota = int(input("Nota "))
            note.update(({"Nota ": nota}))

    registru.append(elev_materie)
    registru.append(note)

for aa1 in range(0, d):
    numestudenti = input("Numele ")
    elev_materie1.update({"Nume": numestudenti})

    for aa2 in range(0, e):
        obiect = input("Materie ")
        elev_materie1.update({"Materie ": obiect})

        for aa3 in range(0, f):
            nota = int(input("Nota "))
            note1.update(({"Nota ": nota}))

    registru1.append(elev_materie1)
    registru1.append(note1)

for a1a in range(0,d):
    numestudenti = input("Numele ")
    elev_materie2.update({"Nume": numestudenti})

    for a2a in range(0,e):
        obiect = input("Materie ")
        elev_materie2.update({"Materie ": obiect })

        for a3a in range(0,f):
            nota = int(input("Nota "))
            note2.update(({"Nota ": nota}))

    registru2.append(elev_materie2)
    registru2.append(note2)

for a1aa in range(0,d):
    numestudenti = input("Numele ")
    elev_materie3.update({"Nume": numestudenti})

    for a2aa in range(0,e):
        obiect = input("Materie ")
        elev_materie3.update({"Materie ": obiect })

        for a3aa in range(0,f):
            nota = int(input("Nota "))
            note3.update(({"Nota ": nota}))

    registru3.append(elev_materie3)
    registru3.append(note3)

print(registru)
print(registru1)
print(registru2)
print(registru3)



