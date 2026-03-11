import multiDictionary as md
m = md.MultiDictionary()

import dictionary as di
d = di.Dictionary()

class RichWord:
    def __init__(self, parola: str, corretta, lista: list, flag: int, count: int, temp: di): #linguaggio: str
        self.parola = parola # this is a string
        self.lista = lista
        self.flag = flag
        self.count = count
        self.temp = temp
        self._corretta = None #this is a bool
        self.corretta = corretta

    @property
    def corretta(self):
        return self._corretta

    @corretta.setter
    def corretta(self, boolValue):
        if self.flag == 0:
            boolValue = self.temp.__contains__(self.parola)
            if boolValue == False:
                print(self.parola)
                self.count = self.count + 1
            self._corretta = boolValue

        if self.flag == 1:
            boolValue = m.searchWordLineare(self.lista, self.parola)
            if boolValue == False:
                print(self.parola)
                self.count = self.count + 1

        if self.flag == 2:
            boolValu = m.searchWordDicotomica(self.lista, self.parola)
            if boolValu == False:
                print(self.parola)
                self.count = self.count + 1

    def __str__(self):
        if self.corretta == False:
            return self.parola
        return None

    def counter(self):
        return self.count