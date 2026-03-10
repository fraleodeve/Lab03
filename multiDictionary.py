import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self, words: str, language: str):
        self.words = words
        self.language = language

    def printDic(self):
        lingua = self.language.capitalize() + ".txt"
        d.Dictionary(self.words, None, lingua)
        lista = d.Dictionary(self.words, None, lingua)
        for element in lista:
            print(element)

    def searchWord(self, word, language):
        lingua = language.capitalize() + ".txt"
        lista = d.Dictionary(word, None, lingua)
        for el in lista:
            if el == self.words:
                return True
        return False



