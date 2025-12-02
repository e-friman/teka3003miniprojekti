class FilterBuilder:
    def __init__(self, syote = input):
        self._input = syote


    def get_key(self):
        #Korjatkaa kieliasua jos jaksatte
        return self._input("Anna hakukenttä: ")

    def get_value(self):
        return self._input("Anna hakukentän arvo: ")

    def read_input(self):
        filt = {}
        while True:
            key = self.get_key()
            if not key:
                return filt
            value = self.get_value()
            #Sallitaan toistaiseksi tyhjät kentät esim "author": ""
            filt[key] = value
