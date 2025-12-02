import os
from citation import Citation
from database import DatabaseHandler
from lomake import Lomake
from filter_builder import FilterBuilder

citation1 = Citation("article", "key1", {"author": "author", "title": "title"})


db = DatabaseHandler()
db.add(citation1)

lomake = Lomake()

entryt = lomake.entry_tyypit


def main():

    #Ohjelma käynnistyy
    syote = lue_syote()

    #Main loop (kts. tkinter myöhemmin?)
    while syote != "q":
        if syote == "1":
            #testidata, tähän joku getData() tms.
            try:
                cit = lomake.tayta_lomake(None)
                db.add(cit)
            except RuntimeError as e:
                print(str(e))
        elif syote == "2":
            for c in db.get_all():
                print(str(c))
        elif syote =="3":
            for citation in db.get_all():
                print(citation.to_bibtex())
        elif syote =="4":
            fb = FilterBuilder()
            filt = fb.read_input()
            for citation in db.hae_viitteet(filt):
                print(citation.to_bibtex())
        else:
            print(
                "Outo komento!\n")
        input("Paina enter-näppäintä jatkaaksesi")
        syote = lue_syote()

    #Ohjelma sulkeutuu
    print("Ohjelma sulkeutuu!")



def lue_syote():
    clear()
    #Pylint ei tykkää tuosta globalista, pitää muuttaa myöhemmin tms. -Vilppu
    #Vaihdoin tämän taas 1 ja 2 koska en jaksa kirjoittaa -Vilppu
    print(
        "\n"
        "Tervetuloa! Anna Komento!\n"
        "q = Poistu, 1 = Syötä viite, 2 = Hae viitteet,"
        "3 = Tulosta BibTeX-muodossa, 4 = Rajoita hakua"
        )
    inp = input("Komento: ")
    return inp

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
