class Vehicle:
    def __init__(self, brand, model, type):
        self.brand = brand
        self.model = model
        self.type = type
        self.gas_tank_size = 14
        self.fuel_level = 0
        self.mpg = 50

    def calculateGallons(self, driven):
        return self.gas_tank_size - driven/self.mpg

    def fuel_up(self):
        self.fuel_level = self.gas_tank_size
        print('Gas tank is now full.')

    def drive(self, miles):
        print(f'The {self.model} is now driving.')
        self.update_fuel_level(self.calculateGallons(miles))
        print(f"The fuel level is now {self.fuel_level}")

    def update_fuel_level(self, new_level):
        if new_level <= self.gas_tank_size:
            self.fuel_level = new_level
        else:
            print('Exceeded capacity')

    def get_gas(self, amount):
        if (self.fuel_level + amount <= self.gas_tank_size):
            self.fuel_level += amount
            print('Added fuel.')
        else:
            print('The tank won\'t hold that much.')

def main():
    myCar = Vehicle('Honda', 'Civic', '4-Door')
    myCar.fuel_up()
    myCar.drive(50)

if __name__ == "__main__":
    main()


class ElectricVehicle(Vehicle):
    def __init__(self, brand, model, type):
        super().__init__(brand, model, type)
        self.charge_level = 390
        self.__charge_max = 390

    def calculateGallons(self, driven):
        print('This vehicle has no fuel tank!')

    def calculateCharge(self, driven):
        self.charge_level -= driven
        return self.charge_level

    def charge(self):
        self.charge_level = self.__charge_max
        print(f'The vehicle is now charged with a range of 
{self.charge_level} miles')

    def fuel_up(self):
        print('This vehicle has no fuel tank!')

    def drive(self, miles):
        print(f"The {self.brand} {self.model} has driven {miles} miles and 
has a charge of {self.calculateCharge(miles)}")

myTesla = ElectricVehicle('Tesla', 'Model S', '4-door')

myTesla.charge()
myTesla.drive(300)
print(myTesla.type) 
