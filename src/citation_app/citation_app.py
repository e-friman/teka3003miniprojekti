import os
#from citation import Citation
from database import DatabaseHandler
from lomake import Lomake
from filter_builder import FilterBuilder

class CitationApp:
    def __init__(
            self, db = DatabaseHandler(),
            input_ = input,
            print_ = print,
            clear = True
            ):
        self._input = input_
        self._print = print_
        self._db = db
        self._clear = clear

    def run(self):

        #Ohjelma käynnistyy
        syote = self.lue_syote()
        lomake = Lomake(self._input)

        #Main loop (kts. tkinter myöhemmin?)
        while syote != "q":
            if syote == "1":
                #testidata, tähän joku getData() tms.
                try:
                    cit = lomake.tayta_lomake(None)
                    self._db.add(cit)
                except RuntimeError as e:
                    self._print(str(e))
            elif syote == "2":
                for c in self._db.get_all():
                    self._print(str(c))
            elif syote =="3":
                for citation in self._db.get_all():
                    self._print(citation.to_bibtex())
            elif syote =="4":
                fb = FilterBuilder(self._input)
                filt = fb.read_input()
                for citation in self._db.hae_viitteet(filt):
                    self._print(citation.to_bibtex())
            else:
                self._print(
                    "Outo komento!\n")
            self._input("Paina enter-näppäintä jatkaaksesi")
            syote = self.lue_syote()

        #Ohjelma sulkeutuu
        self._print("Ohjelma sulkeutuu!")

    def lue_syote(self):
        self.clear()
        #Pylint ei tykkää tuosta globalista, pitää muuttaa myöhemmin tms. -Vilppu
        #Vaihdoin tämän taas 1 ja 2 koska en jaksa kirjoittaa -Vilppu
        self._print(
            "\n"
            "Tervetuloa! Anna Komento!\n"
            "q = Poistu, 1 = Syötä viite, 2 = Hae viitteet,"
            "3 = Tulosta BibTeX-muodossa, 4 = Rajoita hakua"
            )
        inp = self._input("Komento: ")
        return inp

    def clear(self):
        if self._clear:
            os.system('cls' if os.name == 'nt' else 'clear')
