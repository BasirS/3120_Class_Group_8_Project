# This is the parent class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self, sound):
        return f"This animal says {sound}"

    def describe(self):
        return f"{self.name} is a {self.species}."

    def eat(self, food):
        return f"{self.name} is eating {food}."

    def sleep(self):
        return f"{self.name} is now sleeping."
        
    def play(self):
        return f"{self.name} is playing."