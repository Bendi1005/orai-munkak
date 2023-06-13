class Fogadasi_fordulo:
    def __init__(self, row) -> None:
        splitted = row.split(';')
        self.Év = int(splitted[0])
        self.Hét = int(splitted[1])
        self.Forduló = int(splitted[2])
        self.T13p1 = int(splitted[3])
        self.Ny13p1 = int(splitted[4])
        self.Eredmények = splitted[5]



