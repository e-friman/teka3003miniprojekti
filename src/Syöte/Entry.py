class Entry:
        #aloitetaan kysymällä entry tyyppiä esim book (@book)
    def entrySyöte():
        entry = input("Entry-tyyppi = ")
        return entry
    
    #jokin rakenne esim dict missä on entry tyyppien syötteet
    #esim. book = [author, title, publisher, year]
    entryTyypit={
        "article": ["author", "title", "journal", "year"],
        "book": ["author", "title", "publisher", "year"]
        #jne.
    }