'''
File: enclosure.py
Description: A brief description of this Python module.
Author: Shahab Moradi
ID: 1104436331
Username: morsy065
This is my own work as defined by the University's Academic Integrity Policy.
'''
# Enclosure main class with encapsulated attributes
class Enclosure:
    def __init__(self, habitat_type, size):
        self.__habitat_type = habitat_type
        self.__size = size
        self.__cleanliness_level = 100
        self.__animals = []
    # list method 
    def list_animals(self):
        if not self._Enclosure__animals:
            return f"No animals in the {self.__habitat_type} enclosure."
        return [f"{animal.get_name()} ({animal.get_species()})" for animal in self.__animals]
    
class Savannah(Enclosure):
    def __init__(self, size):
        super().__init__("Savannah", size)

    def add_animal(self, animal):
        if animal.get_type() != "Savannah":
            return f"Cannot add {animal.get_species()} to a Savannah enclosure!"
        self._Enclosure__animals.append(animal)
        return f"{animal.get_name()} the {animal.get_species()} has been added to the Savannah enclosure."

    def status(self):
        return (
            f" Savannah Enclosure (Size): {self._Enclosure__size} m² \n Cleanliness: {self._Enclosure__cleanliness_level}/100 \n Animals: {len(self._Enclosure__animals)} \n ---------")

class Aquatic(Enclosure):
    def __init__(self, size):
        super().__init__("Aquatic", size)

    def add_animal(self, animal):
        if animal.get_type() != "Aquatic":
            return f"Cannot add {animal.get_species()} to an Aquatic enclosure."
        self._Enclosure__animals.append(animal)
        return f"{animal.get_name()} the {animal.get_species()} has been added to the Aquatic enclosure."

    def status(self):
        return (
            f" Aquatic Enclosure - Size: {self._Enclosure__size} m² \n Cleanliness: {self._Enclosure__cleanliness_level}/100 \n Animals: {len(self._Enclosure__animals)} \n ---------")

class Forest(Enclosure):
    def __init__(self, size):
        super().__init__("Forest", size)

    def add_animal(self, animal):
        if animal.get_type() != "Forest":
            return f"Cannot add {animal.get_species()} to a Forest enclosure."
        self._Enclosure__animals.append(animal)
        return f"{animal.get_name()} the {animal.get_species()} has been added to the Forest enclosure."

    def status(self):
        return (
            f" Forest Enclosure - Size: {self._Enclosure__size} m² \n Cleanliness: {self._Enclosure__cleanliness_level}/100 \n Animals: {len(self._Enclosure__animals)} \n ---------")