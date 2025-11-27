from citation import Citation
from database import MemoryDatabase
from lomake import Lomake

citation = Citation("article", "key1", {"author": "author", "title": "title"})


db = MemoryDatabase()
db.add(citation)

lomake = Lomake()

entryt = lomake.entry_tyypit



print(db.get_all())
print(str(db.get_all()[0]))

def tervetuloa():
    #Pylint ei tykkää tuosta globalista, pitää muuttaa myöhemmin tms. -Vilppu
    #Vaihdoin tämän taas 1 ja 2 koska en jaksa kirjoittaa -Vilppu
    print(
        "\n"
        "Tervetuloa! Anna Komento!\n"
        "1 = Syötä viite, 2 = Poistu")
    inp = input("Komento:")
    return inp


#Ohjelma käynnistyy
syote = "0"

#Main loop (kts. tkinter myöhemmin?)
while syote != "2":
    syote = tervetuloa()
    if syote == "1":
        #testidata, tähän joku getData() tms.
        cit = lomake.tayta_lomake(None)
        print(str(cit))
        db.add(cit)
    elif syote == "3":
        for c in db.get_all():
            print(str(c))
    else:
        print(
            "Outo komento!\n")

#Ohjelma sulkeutuu
print("Ohjelma sulkeutuu!")
