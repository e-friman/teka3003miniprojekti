class lomake:
    #kysy käyttäjältä lomakkeen sisältö
    def kysySyotetta(obj):
        syote = input(str(obj) + " = ")
        return syote
    
    def haeKentät(dict, syöte):
        ent = dict[syöte]
        return ent

    #kysyy lomakkeen sisällön käyttäjältä ja laittaa sen eteenpäin tallennettavaksi
    def taytaLomake(entryTyyppi):
        for obj in entryTyyppi:
            lomake.kysySyotetta(obj)
        #lahetaLomakeTallennettavaksi(entryTyyppi, syote)


    #kysytään entryn kenttiä vastaavat pakolliset tiedot

    #tätä ei ainakaan toistaiseksi käytetä
    '''
    def kysyPakolliset(list):
        #luodaan uusi lista
        newList = []
        for obj in list:
            syöte = Syöte.kysySyötettä(obj)
            newList.append( obj + "=" + syöte) 
        return newList
    '''