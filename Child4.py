
# Child class inheriting from Animal

from Animal import Animal

class Tiger(Animal):
    def __init__(self, name, species="Tiger", stripe_pattern="striped"):
        # Call the parent class constructor
        super().__init__(name, species)
        self.stripe_pattern = stripe_pattern  # Attribute for tiger's stripe pattern

    def make_sound(self, sound="roar"):
        return f"{self.name}, the {self.species}, lets out a mighty {sound}!"

    def hunt(self):
        return f"{self.name} is silently stalking its prey in the jungle."

    def pounce(self):
        return f"{self.name} leaps swiftly and powerfully!"

    def sleep(self):
        return f"{self.name} is resting after a long hunt in the jungle."


if __name__ == "__main__":
    my_tiger = Tiger("Shere Khan")
    print(my_tiger.describe())
    print(my_tiger.make_sound())
    print(my_tiger.sleep())
    print(my_tiger.hunt())
    print(my_tiger.pounce())

