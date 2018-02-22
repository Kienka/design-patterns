class Flys:

    def fly(self):
        return "May Can Fly"

class ItFlys(Flys):
    def fly(self):
        return "It can fly"

class CantFly(Flys):
    def fly(self):
        return "Cant fly"

class Animal:
    def __init__(self):
        self.flyingType = Flys()

    def tryToFly(self):
        return self.flyingType.fly()

    def setFlyingAbility(self,Flys):
        self.flyingType = Flys()

class Dog(Animal):

    def __init__(self):
        super().__init__()
        self.flyingType = CantFly()

class Bird(Animal):
    def __init__(self):
        super().__init__()
        self.flyingType = ItFlys()



spook = Dog()
print(spook.tryToFly())
spook.setFlyingAbility(ItFlys)
print(spook.tryToFly())

