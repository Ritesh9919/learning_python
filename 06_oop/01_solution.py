class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1
        
    def print_car_info(self):
            return f"{self.model} {self.brand}"
        
    def get_brand(self):
        return self.__brand     
    
    def fuel_type(self):
        return "Petrol or Diesel"
    @staticmethod
    def general_desc():
        return "Car are means of transport"
    @property
    def model(self):
        return self.__model
        
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        self.battery_size = battery_size
        super().__init__(brand, model)
        
    def fuel_type(self):    
        return "Electric charge"


  
# print(my_tesla.__brand)
# print(my_tesla.print_car_info())     
# my_car = Car("Audi", "m1") 
# print(my_car.model) 
# print(my_car.print_car_info())  
# my_new_car = Car("Tata", "Safari")
# print(my_new_car.model)
# print(my_tesla.fuel_type())
# safary = Car("Tata", "Safary")
# print(Car.total_car)
# print(safary.fuel_type())

# my_car = Car("test", "test")
# my_tesla = ElectricCar("Tesla", "Model s", "45kph")
# print(isinstance(my_tesla, Car)) 
# print(isinstance(my_tesla, ElectricCar))
# print(Car.general_desc())
# print(my_car.model)
# my_car.model = "test1"
# print(my_car.model)


class Battery:
    def battery_info(self):
        return "this is battery"
    
    
class Engine:
    def engine_info(self):
        return "this is engine info"

class ElectricCarTwo(Battery, Engine, Car):
    pass
    
        
my_new_tesla = ElectricCarTwo("tasla", "model s")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())