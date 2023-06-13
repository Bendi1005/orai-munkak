class Result:
    def __init__(self, row) -> None:
        splitted = row.split(' ')
        self.place = int(splitted[0])
        self.members = int(splitted[1])
        self.sport = splitted[2]
        self.kind = splitted[3]

    def point(self):
        if self.place == 1:
            return 7
        elif self.place == 2:
            return 5
        elif self.place == 3:
            return 4
        elif self.place == 4:
            return 3    
        elif self.place == 5:
            return 2
        else:
            return 1