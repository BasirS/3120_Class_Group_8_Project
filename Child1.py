# This is child class #1
from Animal import Animal

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Dog")
        self.favorite_toy = "Bone"

    def make_sound(self, sound = "Woof"):
        return sound
    
    def play(self):
        print(f"{self.name} is playing with {self.favorite_toy}.")

# main function
if __name__ == "__main__":
    d = Dog("Rex")
    print(d.make_sound())
    print(d.describe())
    print(d.eat("Dog food"))
    print(d.play())
    print(d.sleep())