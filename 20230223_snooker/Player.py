class Player:
    def __init__(self, row) -> None:
        splitted = row.split(';') 
        self.Position = int(splitted[0])
        self.Name = splitted[1]
        self.Country = splitted[2]
        self.Prize = int(splitted[3])




