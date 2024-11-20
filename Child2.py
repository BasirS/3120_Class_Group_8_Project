# This is child class #2
from Animal import Animal

class Cat(Animal):
    def __init__(self, name, species = "Cat"):
        super().__init__(name, species)
        self.favorite_toy = "Feather"

    def make_sound(self):
        return "Meow!"

    def nap(self):
        print(f"{self.name} is now napping after playing with {self.favorite_toy}.") 

# main function
if __name__ == "__main__":
    c = Cat("Whiskers")
    print(c.make_sound())
    print(c.describe())
    print(c.eat("Cat food"))
    print(c.play())
    print(c.nap())