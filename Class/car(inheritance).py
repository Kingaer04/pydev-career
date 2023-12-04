class Car:
    def __init__(self, make:str, model:str, year:int, odometer_reading:int=0, increment:int=1) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = odometer_reading
        self.increment = increment

    def fill_tank(self):
        print('This car uses gas tank')

    def get_descriptive_name(self) -> str:
        return '*********Car details*********\n\tName: {}\t\n\tModel: {}\t\n\tYear: {}\t'.format(self.make,self.model,self.year)
    
    def read_odometer(self) -> str:
        return f'This car has {str(self.odometer_reading)} miles on it'
    
    def update_odometer(self) -> None:
        self.value += self.increment


class Battery:
    def __init__(self, batterysize:int=70):
        self.batterysize = batterysize

    def describe_battery(self) -> str:
        return f'This car has {str(self.batterysize)} -kwh battery'

class ElectricCar(Car):
    def __init__(self, make, model, year) -> None:
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_tank(self):
        print('This car does not uses gas tank!')    


car = ElectricCar('Tesla', 'wegot456', 2019)
print(car.get_descriptive_name())
print(car.battery.describe_battery())

