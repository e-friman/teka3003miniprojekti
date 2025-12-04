#from citation import Citation
from database import DatabaseHandler
from lomake import Lomake
from filter_builder import FilterBuilder

class CitationApp:
    def __init__(
            self, db = DatabaseHandler(),
            input_ = input,
            print_ = print
            ):
        self._input = input_
        self._print = print_
        self._db = db

    def run(self):

        #Ohjelma käynnistyy
        lomake = Lomake(self._input)
        ohjeet = (
                "q = Poistu, 1 = Syötä viite, 2 = Hae viitteet,"
                "3 = Tulosta BibTeX-muodossa, 4 = Rajoita hakua"
                )
        self._print("Tervetuloa! Anna Komento!\n")
        self._print(ohjeet)
        syote = self.lue_syote()

        #Main loop (kts. tkinter myöhemmin?)
        while syote != "q":
            if syote == "1":
                #testidata, tähän joku getData() tms.
                try:
                    cit = lomake.tayta_lomake()
                    self._db.add(cit)
                except ValueError as e:
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
                self._print(ohjeet)
            syote = self.lue_syote()

        #Ohjelma sulkeutuu
        self._print("Ohjelma sulkeutuu!")

    def lue_syote(self):
        inp = self._input("Komento: ")
        return inp
