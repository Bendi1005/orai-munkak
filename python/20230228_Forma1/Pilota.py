class Pilota:
    def __init__(self, row:str) -> None:
        splitted = row.split(';')
        self.name = splitted[0]
        self.birthDate = splitted[1]
        self.country = splitted[2]
        self.startNumber = splitted[3]

        splittedYear = self.birthDate.split('.')
        self.year = int(splittedYear[0])