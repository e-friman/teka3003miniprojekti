from Entry import Entry
from Lomake import Lomake

Entry() == Entry
Lomake() == Lomake
#ohjelman käynnistyessä kysytään käyttäjältä komento
def tervetuloa():
    global syote
    #Vaihdoin tämän taas 1 ja 2 koska en jaksa kirjoittaa -Vilppu
    print("Tervetuloa! Anna Komento!\n" \
    "1 = Syötä viite, 2 = Poistu")
    syote = input("Komento:")
    return syote

def syotaViite(dict):
    entry = Entry.entrySyote()
    list = Lomake.haeKentat(dict, entry)
    Lomake.taytaLomake(list)


#Ohjelma käynnistyy
syote = tervetuloa()

#Main loop (kts. tkinter myöhemmin?)
while(syote != "2"):
    if(syote == "1"):
        #testidata, tähän joku getData() tms.
        data = Entry.entryTyypit
        syotaViite(data)
        syote = tervetuloa()
    else:
        print("Outo komento!")
        syote = tervetuloa()

#Ohjelma sulkeutuu
print("Ohjelma sulkeutuu!")
quit()