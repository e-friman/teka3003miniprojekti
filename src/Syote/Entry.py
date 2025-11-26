class Entry:
        #aloitetaan kysymällä entry tyyppiä esim book (@book)
    def entrySyote():
        entry = input("Entry-tyyppi = ")   
        return entry
    
    #Dictionary missä on entry tyyppien syötteet
    #esim. book = [author, title, publisher, year]
    #Oikeasti otetaan databasesta ym.
    entryTyypit={
        "article": [
            "author","title","journal","year"
            ],
        "book": [
            "author","title","publisher","year"
            ]
        #jne.
    }