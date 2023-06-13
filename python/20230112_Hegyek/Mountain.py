class mountain:
    def __init__(self, row:str) -> None:
        splitted = row.split(';')
        self.name = splitted[0]
        self.mountainRange = splitted[1]
        self.height = int(splitted[2])




































