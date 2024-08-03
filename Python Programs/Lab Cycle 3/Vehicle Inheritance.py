class Vehicle:
    def __init__(self, make, model, year, fuel):
        self.manufact = make
        self.model = model
        self.year = year
        self.fuel = fuel

    def refuel(self, liters):
        self.fuel += liters

    def drive(self, distance):
        print(f'Driving {distance} kms.',end = '')
        print(f'Fuel Remaining: {float(self.fuel)} liters.')

class Car(Vehicle):
    def __init__(self, make, model, year, fuel, num_doors):
        super().__init__(make, model, year, fuel)
        self.num_doors = num_doors

    def honk(self):
        print('Honk! Honk!')

class Bicycle(Vehicle):
    def __init__(self, make, model, year, fuel, num_gears):
        super().__init__(make, model, year, fuel)
        self.num_gears = num_gears

    def bell(self):
        print('Ring, ring!')

class MotorCycle(Vehicle):
    def __init__(self, make, model, year, fuel, engine_displace):
        super().__init__(make, model, year, fuel)
        self.engine_displace = engine_displace

    def start_engine(self):
        print('Starting Motorcycle Engine...')
        

print('Car:')
car = Car('Toyota','Camry',2023,10,4)
car.drive(50)
car.honk()
print()
print('Bicycle:')
bicycle = Bicycle('Terminator','Hercules',2016,0,4)
bicycle.drive(10)
bicycle.bell()
print()
print('Motorcycle:')
mcycle = MotorCycle('Platina','Bajaj',2022,10,100)
mcycle.drive(25)
mcycle.start_engine()
        
