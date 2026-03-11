import dictionary as di
d = di.Dictionary()
import richWord as rw

class MultiDictionary:

    def __init__(self):
        self.words = None
        self.language = None

    def printDic(self):
        lista = d.loadDictionary(self.language)
        for element in lista:
            print(element)

    def searchWordLineare(self, lista, word): # linguaggio
        for el in lista:
            if el == word:
                return True
        return False

    def searchWordDicotomica(self, lista, word):
        sinistra = 0
        destra = len(lista) - 1
        while sinistra <= destra:
            medio = (sinistra + destra) // 2
            if lista[medio] == word:
                return True
            elif lista[medio] < word:
                sinistra = medio + 1
            else:
                destra = medio - 1
        return False


