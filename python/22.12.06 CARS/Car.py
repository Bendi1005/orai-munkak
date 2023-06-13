class Car:
    def __init__(self, row: str):
        #PlateNumber;Brand;Year;Cm3;Price;Doors;Speed;HP;Consumption;Color;FirstOwner
        splitted = row.split(';')
        self.PlateNumber = splitted[0]
        self.Brand = splitted[1]
        self.Year = int(splitted[2])
        self.Cm3 = int(splitted[3])
        self.Price = float(splitted[4])
        self.Doors = int(splitted[5])
        self.Speed = int(splitted[6])
        self.HP = int(splitted[7])
        self.Consumption = float(splitted[8])
        self.Color = splitted[9]
        if splitted[10] == '0':
            self.FirstOwner = False
        else:
            self.FirstOwner = True




