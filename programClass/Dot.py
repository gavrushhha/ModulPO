class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, dot):
        return self.x == dot.x and self.y == dot.y
    def __lt__(self, dot):
        return self.x < dot.x and self.y < dot.y
    def __gt__(self, dot):
        return self.x > dot.x and self.y > dot.y
    def __add__(self, dot):
        return Dot(self.x + dot.x, self.y + dot.y)
    def __sub__(self, dot):
        return Dot(self.x - dot.x, self.y - dot.y)
    def __le__(self, dot):
        return (self.x == dot.x and self.y < dot.y) or (self.y == dot.y and self.x < dot.x)   
    def __le__(self, dot):
        return (self.x == dot.x and self.y > dot.y) or (self.y == dot.y and self.x > dot.x)   
dot1 = Dot(1, 2)
dot2 = Dot(3, 4)
print(dot1 > dot2)    
