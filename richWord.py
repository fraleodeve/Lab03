import multiDictionary as md
m = md.MultiDictionary()

class RichWord:
    def __init__(self, parola: str, corretta: None, linguaggio: str):
        self.parola = parola # this is a string
        self.linguaggio = linguaggio
        self._corretta = None #this is a bool
        self.corretta = corretta


    @property
    def corretta(self):
        # print("getter of parola called" )
        return self._corretta

    @corretta.setter
    def corretta(self, boolValue):
        boolValue = m.searchWord(self.linguaggio, self.parola)
        # print("setter of parola called" )
        self._corretta = boolValue

    def __str__(self):
        if self.corretta == False:
            return self.parola