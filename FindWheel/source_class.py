
class Vehicle:                           # Parent class
    def __init__(self, model, wheel, engine, mileage):
        self.model = model
        self.no_of_wheels = wheel
        self.engine_power = engine
        self.mileage = mileage

    def model_name(self):
        return f"This is {self.model},"

    def check_wheels(self):     
        if self.no_of_wheels == 2:
            say = "a bike."
        elif self.no_of_wheels == 4:
            say = "a car."
        else:
            say = "a commercial vehicle."
        return say

    def specifications(self):
        return f"Specs are: engine -> {self.engine_power} HP, mileage -> {self.mileage} KMPL."


class Bike(Vehicle):
    # def __init__(self, model, wheel : int, engine : int, mileage : int):
    def about_bike(self):  
        about = f"{self.model_name()} {self.check_wheels()} {self.specifications()}"
        return about

class Car(Vehicle):
    def about_car(self):  
        about = f"{self.model_name()} {self.check_wheels()} {self.specifications()}"
        return about

class Commercial(Vehicle):
    def about_commercial(self):
        is_truck = input("Is it a truck: (T)rue / (F)alse : ")
        if is_truck.lower() == 't':
            say = "\nWelcome to your lorry ! here is more about it...\n"
            return F"{say}{self.model_name()} {self.check_wheels()} {self.specifications()} "
        else:
            say = "Sorry! Currently we accept 'truck' only."
            return f"{say} "

            