import resources

class Dictionary:
    def __init__(self):
        self.lista = []

    def loadDictionary(self, path) -> list:
        percorso = path.capitalize() + ".txt"
        file = "resources" + "/" + percorso
        infile = open(file, "r", encoding="utf-8")
        lines = infile.readlines()
        for i in range(0, len(lines)):
            temp = lines[i]
            variabile = temp.strip("\n")
            self.lista.append(variabile)
        return self.lista


    def printAll(self):
        for el in self.lista:
            print(el)

    @property
    def dict(self) -> list:
        return self.lista

    def __contains__(self, item):
        if item in self.lista:
            return True
        return False