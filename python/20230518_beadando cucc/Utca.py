class Utca:
    def __init__(self, row:str) -> None:
        splitted = row.split(' ')
        self.adoszam = int(splitted[0])
        self.utca = splitted[1]
        self.hazszam = splitted[2]
        self.adosav = splitted[3]
        self.terulet = splitted[4]