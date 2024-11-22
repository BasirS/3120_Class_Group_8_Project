from Animal import Animal

def Elephant(Animal):
	def __init__(self,name,species="Elephant"):
		super().__init__(name,species)
		self.biggest_fear="Mouse"

	def make_sound(self):
		return "*insert elephant honk here*"

	def stomp(self):
		return "{self.name} panickedly stomps their feet, narrowly missing crushing your poor pitiable human form."

# main

if __name__== "__main__":
	e1=Elephant("Jumbo")
	print(e1.describe())
	print(e1.make_sound())
	print(e1.stomp())
