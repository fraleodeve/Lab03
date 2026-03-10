import multiDictionary as md

class RichWord:
    def __init__(self, parola: str, language: str, corretta: None):
        self.language = language
        self.parola = parola # this is a string
        self._corretta = None #this is a bool
        self.corretta = corretta

    def booleanv(self):
        boolValue = md.MultiDictionary.searchWord(self.parola, self.language)
        return boolValue

    @property
    def corretta(self):
        # print("getter of parola called" )
        return self._corretta

    @corretta.setter
    def corretta(self, boolValue):
        #boolValue = md.MultiDictionary.searchWord(self, self.language, self._parola)
        boolValue = self.booleanv()
        # print("setter of parola called" )
        self._corretta = boolValue

    def __str__(self):
        return self._parola