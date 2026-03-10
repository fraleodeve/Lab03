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

    def searchWord(self, language, word):
        lista = d.loadDictionary(language)
        for el in lista:
            if el == word:
                return True
        return False



