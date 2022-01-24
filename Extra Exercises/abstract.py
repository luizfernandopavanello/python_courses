"""
Prevents a user from creating an object of that class
+ compels a usar to override abstract methods in a child class

abstract class = a class which contains one or more abstract methods;
abstract method = a method that has a declaration but does have am implementation
"""

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")

class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("You stop the motorcycle")


# vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

# vehicle.go()
car.go()
motorcycle.go()

car.stop()
motorcycle.stop()