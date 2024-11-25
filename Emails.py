# class Dog:
#     species = "Canis familiaris"

#     def __init__(self, name, age):
#         print(name)
#         self.name = name
#         self.age = age
    
#     def getName(self):
#         return self.name
    
#     def __str__(self):
#         return (f"{self.name} is {self.age} years old")
    
#     def speak(self, sound):
#         return (f"{self.name} says {sound}")
    
# myFamilyDog = Dog("Buddy", 9)
# print(myFamilyDog)

# myDog = Dog("Mimi", 8)
# myFamilyDog.speak("gibs chimkin")
# myDog.speak("give treats")

class Emails:

    def __init__(self):
        self.__contacts = { 'unga': 'unga@unga.com'}
        self.main()

    def lookupEmail(self): #
        email = input("Enter a name to search: ")
        return self.__contacts.get(email, False)

    def addEmail(self):
        name = input("Enter a name to add: ")
        email = input("Enter the email to add: ")
        self.__contacts.update({name: email})
        return self.__contacts

    def updateEmail(self):
        name = input("Enter a name to change: ")
        email = input("Enter the email to add: ")
        self.__contacts.update({name: email})
        return self.__contacts

    def deleteEmail(self):
        name = input("Enter a name to delete: ")
        del self.__contacts[name]
        return self.__contacts

    def main(self):
        choice = input("L: to lookup, A to add, U to update, and D to delete: Q to quit. ").lower()
        
        while choice != "q":
            if choice == "l":
                print(self.lookupEmail())
            elif choice == "a":
                print(self.addEmail())
            elif choice == "u":
                print(self.updateEmail())
            elif choice == "d":
                print(self.deleteEmail())
            else:
                print('Invalid Entry')
                
            choice = input("L: to lookup, A to add, U to update, and D to delete: Q to quit. ").lower()

def main():
    email = Emails()


if __name__ == "__main__":
    main()