class Tanulo:
    def __init__(self, row:str) -> None:
        splitted = row.split(';')
        self.ev = int(splitted[0])
        self.osztaly = splitted[1]
        self.nev = splitted[2]
    def nevHossz(self):
        return len(self.nev.replace(' ',''))

    def azonosito(self):
        splitted = self.nev.split(' ')
        vezeteknev = splitted[0]
        keresztnev = splitted[1]
        azon = str(self.ev)[-1] + self.osztaly + vezeteknev[0:3] + keresztnev[:3]
        return azon.lower()

