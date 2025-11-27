from citation import Citation
class Lomake:
    def __init__(self, syote = input):
        self._input = syote

    #HUOM! siirsin entryn omasta paketista tänne, koska pylint valittaa.
    #Myös korjattu noita selffejä ym. sen verran mitä se kait haluaa.
    #-Vilppu
    #------------------------------------------------------------------
    #aloitetaan kysymällä entry tyyppiä esim book (@book)
    def entry_syote(self):
        entry = self._input("Entry-tyyppi = ")
        return entry

    def key_syote(self):
        return self._input("Anna key: ")
    #Dictionary missä on entry tyyppien syötteet
    #esim. book = [author, title, publisher, year]
    #Oikeasti otetaan databasesta ym.
    entry_tyypit={
        "article": [
            "author","title","journal","year"
            ],
        "book": [
            "author","title","publisher","year"
            ]
        #jne.
    }

    #Hae entryä vastaavat kentät dictionarysta dict
    def hae_kentat(self, db, syote):
        kentat = db[syote]
        return kentat

    #Kysy käyttäjältä lomakkeen sisältö
    def kysy_syotetta(self, field):
        return self._input(str(field) + " = ")

    #Kysyy lomakkeen sisällön käyttäjältä ja laittaa sen eteenpäin tallennettavaksi
    def tayta_lomake(self, data):
        #newList = []
        entry = self.entry_syote()
        key = self.key_syote()
        kentat = self.hae_kentat(self.entry_tyypit, entry)
        data = {}
        for field in kentat:
            #HUOM! Pylint valittaa, että tässä on muka liikaa argumentteja,
            #vaikka se itse haluaa niitä ja koodi ei toimi ilman että tuohonkin
            #laittaa joten enpä tiedä
            #-Vilppu
            out = self.kysy_syotetta(field)
            data[field] = out
            #syote = Lomake.kysySyötettä(obj)
            #newList.append( obj + "=" + syöte)
            #return newList
        return Citation(entry, key, data)
