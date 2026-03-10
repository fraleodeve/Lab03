class Dictionary:
    def __init__(self, parola: str, booleano: bool):
        dict = {}

    def loadDictionary(self, path) -> list:
        infile = open(path, "r", encoding="utf-8")
        lines = infile.readlines()
        for i in range(0, len(lines)):
            lines[i] = lines[i].strip("\n")
            self.lista.append(lines[i])
            #self.parola = lines[i]
            #lista.append(self.parola)
        return self.lista


    def printAll(self):
        pass


    @property
    def dict(self) -> list:
        return self.lista