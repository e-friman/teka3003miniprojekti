from Entry import Entry
from Syöte import Syöte
from tyypit import entryTyypit

Entry() == Entry
Syöte() == Syöte

print(entryTyypit["article"])
print(Syöte.haeKentät(entryTyypit,"book"))
e1 = Entry.entrySyöte()
print(e1)
l1 = Syöte.haeKentät(entryTyypit ,e1)
print(l1)
syötteet = Syöte.kysyPakolliset(l1)
print(syötteet)