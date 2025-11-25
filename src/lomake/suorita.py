from Entry import Entry

#ohjelman käynnistyessä kysytään käyttäjältä komento
def tervetuloa():
        global syote
        print("Tervetuloa! Anna Komento! lomake = käynnistä lomake, poistu = poistu")
        syote = input("Komento:")
        return syote
        
syote = tervetuloa()

while(syote != "poistu"):
        if(syote == "lomake"):
            Entry.entrySyote()
            syote = tervetuloa()
        else:
            print("outo komento!")
            syote = tervetuloa()
    
print("Ohjelma sulkeutuu")
quit()