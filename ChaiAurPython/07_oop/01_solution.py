#Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.

class Car:

    total_car=0

    def __init__(self,brand,model):#constructor
        self.__brand=brand
        self.__model=model
        Car.total_car+=1

    def fullname(self):
       print({f"Brand:{self.__brand}, Model:{self.__model}"})

    def get_brand(self):
        return self.__brand+" !"
    
    def fuel_type(self):
        return "Disel or Petrol"
    
    @staticmethod#decorater
    def general_description():
        return "Cars are making for driving"

    @property
    def model(self):
        return self.__model




# Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.

class ElectricCar(Car) :
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
    def fuel_type(self):
        return "Electric Charge"

# my_tesla=ElectricCar("Tesala","Model S","85KWh")
# print(my_tesla.model)
# print(my_tesla.__brand)
# print(my_tesla.battery_size)
# print(my_tesla.fullname())
# print(my_tesla.get_brand())
# print(my_tesla.fuel_type())

# print(isinstance(my_tesla,Car and ElectricCar))



# tesla=ElectricCar("Tesala","Model B")
# print(my_tesla.fuel_type())
    
# safari=Car("Tata","Safari")
# print(safari.fuel_type())
    
# print(Car.total_car)
# print(Car.general_description())


# my_Car=Car("Tesla","Nexon")
# my_Car.model="City"
# print(my_Car.model)



    
# #object or instance creation
# #sysntax: refvar:classname(attributes_or_variable)

# my_car=Car("Toyota","Corrola")
# print(my_car.brand)
# print(my_car.model)


# my_new_car=Car("TATA","Safari")
# print(my_new_car.brand)

# my_new_car.fullname()


class Battery:
    def battery_info(self):
        return "This is battery"
class Engine:
    def engine_info(self):
        return "This is engine"
class ElectricCar2(Battery,Engine,Car):
    pass

my_new_tesala=ElectricCar2("Tesla","Model S")
print(my_new_tesala.engine_info())
print(my_new_tesala.battery_info())
