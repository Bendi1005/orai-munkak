class Dolgozo:
    def __init__(self, sor:str) -> None:
        splitted = sor.split(';')
        self.nev = splitted[0]
        self.osztaly = splitted[1]
        self.kategoria = int(splitted[2])
        self.koltseg = int(splitted[3])