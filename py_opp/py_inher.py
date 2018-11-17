class Pet(object):
    def __init__(self, name, species): #privite의미를 가짐
        self.name = name
        self.species = species
    def getName(self):
        return self.name
    def getSpecies(self):
        return self.species
    def __str__(self):
        return "동물정보"
class Dog(Pet):
    def __init__(self,bow):
        self.bow = bow
class Cat(Pet):
    def __init__(self,yam):
        self.yam = yam


