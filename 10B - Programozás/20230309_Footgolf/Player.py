class Player:
    def __init__(self, row:str) -> None:
        splitted = row.split(';')
        self.name = splitted[0]
        self.category = splitted[1]
        self.team = splitted[2]
        self.points = []
        for item in splitted[3:]:
            self.points.append(int(item))
        self.firstName = self.name.split(' ')[-1]
        

    def totalPoints(self):
        self.points.sort()
        sum = 0
        for item in self.points[2:]:
            sum += item

        if self.points[0] > 0:
            sum += 10

        if self.points[1] > 0:
            sum += 10

        return sum



