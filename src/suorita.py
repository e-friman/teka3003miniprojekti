from lomake import Lomake

Lomake()
#(fixme):
#Tämä itse suorittaminen halutaan tuolla src/ kansiossa olevassa tiedostossa kuten app.py, niin
#copy-pastesin nyt tämän suorita.py sinne, joten voidaan ajaa sieltä toistaiseksi.
#Myöhemmin tähän halutaan luokka jossa on nuo tervetuloa, syota_viite tms. jota sitten kutsutaan
#siellä ajettavassa. -Vilppu
#
#ohjelman käynnistyessä kysytään käyttäjältä komento
def tervetuloa():
    #Pylint ei tykkää tuosta globalista, pitää muuttaa myöhemmin tms. -Vilppu
    global syote
    #Vaihdoin tämän taas 1 ja 2 koska en jaksa kirjoittaa -Vilppu
    print("Tervetuloa! Anna Komento!\n" \
    "1 = Syötä viite, 2 = Poistu")
    syote = input("Komento:")
    return syote

def syota_viite(db):
    entry = Lomake.entry_syote(Lomake)
    db_data = Lomake.hae_kentat(Lomake, db, entry)
    Lomake.tayta_lomake(Lomake, db_data)

#Ohjelma käynnistyy
syote = tervetuloa()

#Main loop (kts. tkinter myöhemmin?)
while syote != "2":
    if syote == "1":
        #testidata, tähän joku getData() tms.
        data = Lomake.entry_tyypit
        syota_viite(data)
        syote = tervetuloa()
    else:
        print(
            "Outo komento!\n")
        syote = tervetuloa()

#Ohjelma sulkeutuu
print("Ohjelma sulkeutuu!")
#Pylint haluaisi sys.exit mielummin kts. myöhemmin
quit()
