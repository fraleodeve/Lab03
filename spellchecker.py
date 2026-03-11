import time
import richWord as rw
r = rw.RichWord

import dictionary
d = dictionary.Dictionary()

class SpellChecker:

    def __init__(self):
        pass

    def handleSentence(self, txtIn, language):
        print("-" * 30)
        print("Contains")
        start = time.time()
        testo = replaceChars(txtIn).lower()
        parola = testo.split()
        temp = d
        lista = temp.loadDictionary(language)
        flag = 0
        count = 0
        counter = 0
        for ele in parola:
            variabile = r(ele, None, lista, flag, count, temp)
            counter += variabile.counter()
        end = time.time()
        print(f"Parole errate: {counter}")
        print(f"Tempo impiegato: {end - start} secondi")

        print("-"*30)
        print("Ricerca lineare")
        start1 = time.time()
        testo1 = replaceChars(txtIn).lower()
        parola1 = testo1.split()
        lista1 = d.loadDictionary(language)
        flag = 1
        count1 = 0
        counter1 = 0
        for el in parola1:
            variabile1 = r(el, None, lista1, flag, count1, None)
            counter1 += variabile1.counter()
        end1 = time.time()
        print(f"Parole errate: {counter1}")
        print(f"Tempo impiegato: {end1 - start1} secondi")

        print("-" * 30)
        print("Ricerca dicotomica")
        start2 = time.time()
        testo2 = replaceChars(txtIn).lower()
        parola2 = testo2.split()
        lista2 = d.loadDictionary(language)
        flag = 2
        count2 = 0
        counter2 = 0
        for elem in parola2:
            variabile2 = r(elem, None, lista2, flag, count2, None)
            counter2 += variabile2.counter()
        end2 = time.time()
        print(f"Parole errate: {counter2}")
        print(f"Tempo impiegato: {end2 - start2} secondi")


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
    chars = "\\`*_{}[]()>#+-.!?$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text