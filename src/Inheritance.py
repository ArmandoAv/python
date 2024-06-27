# Python can use POO with defined classes

"""
    Classes are defined by class methods and attributes
    Class methods are very similar to functions, 
    but only the self method is called in their definition
"""

class Vehicle:
    # Define the __init__ method with the self method and attributes 
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # Define class methods with the self method
    # With the self method you can use the defined attributes of the class
    def description(self):
        return f"Vehicle: {self.brand} {self.model}"

    # Even if no attribute is used, the self method must be called
    def start(self):
        return "The vehicle is started."

class Car(Vehicle):
    def __init__(self, brand, model, color):
        super().__init__(brand, model)
        self.color = color

    def description(self):
        return f"{super().description()}, Color: {self.color}"

    def start(self):
        return f"{super().start()} The car is ready to drive."

    def engine(self):
        return "Vroom, vroom!"

# Create an instance of the subclass Car
my_car = Car("Toyota", "Corolla", "Red")

# Call the methods of the Car class and the Vehicle class
print(f"Call the methods of the Cars subclass along with the "
       "methods inherited from the Vehicule class\n"
      f"{my_car.description()}")
print(my_car.start())
print(my_car.engine())

# Create an instance of the class Vehicule
my_vehicule = Vehicle("Nissan", "Altima")

# Call the methods of the Car class and the Vehicle class
print(f"\nCall the methods of the class Vehicule \n"
      f"{my_vehicule.description()}")
print(my_vehicule.start())
