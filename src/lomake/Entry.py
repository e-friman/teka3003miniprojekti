from lomake import lomake

class Entry:

        #aloitetaan kysymällä entry tyyppiä esim book (@book)
    def entrySyote():

        lomake()

        #TODO: oma aliohjelma selkeyden vuoksi?
        entryTyypit={
            "article": ["author", "title", "journal", "year"],
            "book": ["author", "title", "publisher", "year"]
            #jne.
        }

        entry = input("Entry-tyyppi = ")
        lomake.taytaLomake(entryTyypit[entry])
        return entry
    
    #jokin rakenne esim dict missä on entry tyyppien syötteet
    #esim. book = [author, title, publisher, year]
    '''
    def setupTyypit():
        entryTyypit={
            "article": ["author", "title", "journal", "year"],
            "book": ["author", "title", "publisher", "year"]
            #jne.
        }
    '''