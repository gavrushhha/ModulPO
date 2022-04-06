class Mashine:
    def __init__(self, power, cost):
        self.power = power
        self.cost = cost

class Driving:
    def __init__(self, speed):
        self.speed = speed
    def move(item, a, b):
        print(f"I moved {item,} from {a} to {b}")

class Washing:
    def __init__(self, time, volume):
        self.time = time
        self.volume = volume
    def wash(self, items, water):
        if len(items) > self.volume:
            print('NOOOOOO')
        else:
            str_items = ', '.join(items)
            print(f'Im washing {str_items} for {self.time} seconds')
class WashingMachine(Washing, Mashine):
    def __init__(self, power, cost, time, volume):
        super().__init__(time, volume) #переопределяем метод 
        self.power= power
        self.cost = cost
    def wash(self, items, water):
        super(). wash(items, water)
        return self.power * self.time

class DrivingMashine(Mashine, Driving):
    def __init__(self, power, cost, speed):
        super().__init__(power, cost)
        self.speed = speed