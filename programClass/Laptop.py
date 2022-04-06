from numpy import diag


class Laptop:
    def __init__(self, diag):
        self.diag = diag
    def __eq__(self, lap):
        return self.diag == lap.diag
    def __lt__(self, lap):
        return self.diag < lap.diag
lap_1 = Laptop(17)
lap_2 = Laptop(19)
print(lap_1 == lap_2)
print(lap_1 < lap_2)