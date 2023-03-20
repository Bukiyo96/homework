import random
a = random.randrange(1,100)
m = int(input("Alege o cifra de la 1 pana la 100:"))

while a != m:
    if m > a:
        print("Prea mult!")
        m = int(input("Alege o alta cifra!"))
    elif m < a:
        print("Prea putin!")
        m = int(input("Alege o alta cifra!"))
    else:
        break
print("Bravo")
