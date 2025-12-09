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
                "q = Poistu, 1 = Syötä viite, 2 = Hae viitteet, "
                "3 = Rajoita hakua, 4 = Tulosta BibTeX-muodossa, "
                "5 = Luo BibTeX-tiedosto, 6 = Synkronoi viitteet"
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
                fb = FilterBuilder(self._input)
                filt = fb.read_input()
                for citation in self._db.hae_viitteet(filt):
                    self._print(citation.to_bibtex())
            elif syote =="4":
                for citation in self._db.get_all():
                    self._print(citation.to_bibtex())
            elif syote =="5":
                #muodostaa .bib tiedoston viitteistä
                filename = self._input("Anna tiedoston nimi: ")
                bibtex = ""

                for citation in self._db.get_all():
                    bibtex += citation.to_bibtex() + "\n"

                if not filename.endswith(".bib"):
                    filename += ".bib"

                with open(filename, "w", encoding="utf-8") as f:
                    f.write(bibtex)
            elif syote =="6":
                path = self._input("Anna tiedostopolku: ")
                
                try:
                    self._db.load_from_file(path)
                except Exception as e:
                    print(e)
                #lataa viitteet käyttäjän antamasta polusta
            else:
                self._print(ohjeet)
            syote = self.lue_syote()

        #Ohjelma sulkeutuu
        self._print("Ohjelma sulkeutuu!")

    def lue_syote(self):
        inp = self._input("Komento: ")
        return inp
