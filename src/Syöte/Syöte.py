class Syöte:
    def kysySyötettä(obj):
        syöte = input(str(obj) + " = ")
        return syöte
    
    def haeKentät(dict, syöte):
        ent = dict[syöte]
        return ent

    #kysytään entryn kenttiä vastaavat pakolliset tiedot
    def kysyPakolliset(list):
        #luodaan uusi lista
        newList = []
        for obj in list:
            syöte = Syöte.kysySyötettä(obj)
            newList.append( obj + "=" + syöte) 
        return newList