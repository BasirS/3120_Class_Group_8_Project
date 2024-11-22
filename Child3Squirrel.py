from Animal import Animal

class Squirrel(Animal):
    def __init__(self, name):
        super().__init__(name, "Squirrel")    
    def climb(self):
        return(f"{self.name} is climbing the {climb_object}.")
    def make_sound(self, sound = "squeeksqueek"):
        return sound

s = Squirrel("Mr.Nut")
climb_object = 'tree'
print(s.make_sound())
print(s.describe())
print(s.eat("nuts"))
print(s.sleep())
print(s.climb())
