import time
import richWord as rw
import multiDictionary as md

import dictionary
d = dictionary.Dictionary

class SpellChecker:

    def __init__(self):
        pass

    def handleSentence(self, txtIn, language):
        #testo = replaceChars(txtIn).lower()
        #parola = testo.split()
        parola = txtIn.split()
        for el in parola:
            rw.RichWord(el, language, None)


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text