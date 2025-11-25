'''
File: staff.py
Description: A brief description of this Python module.
Author: Shahab Moradi
ID: 1104436331
Username: morsy065
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Staff:
    def __init__(self, name, role):
        self.__name = name
        self.__role = role
        self.__assigned_animals = []
        self.__assigned_enclosures = []

    def get_name(self):
        return self.__name

    def get_role(self):
        return self.__role

    def assign_animal(self, animal):
        self.__assigned_animals.append(animal)
        return f"{animal.get_name()} ({animal.get_species()}) assigned to {self.__name}."

    def assign_enclosure(self, enclosure):
        self.__assigned_enclosures.append(enclosure)
        return f"{enclosure._Enclosure__habitat_type} enclosure assigned to {self.__name}."

    def list_animals(self):
        if not self.__assigned_animals:
            return f"{self.__name} has no assigned animals."
        elif self.__assigned_animals:
            return [f"{animal.get_name()} ({animal.get_species()})" for animal in self.__assigned_animals]
        else:
            return "Error!"

    def list_enclosures(self):
        if not self.__assigned_enclosures:
            return f"{self._name} has no assigned enclosures."
        elif self.__assigned_enclosures:
            return [f"{enclosure._Enclosure__habitat_type} (Size: {enclosure._Enclosure__size} m²)" for enclosure in self.__assigned_enclosures]
        else:
            return "Error!"


class Zookeeper(Staff):
    def __init__(self, name):
        super().__init__(name, "Zookeeper")

    def feed_animal(self, animal):
        if animal in self._Staff__assigned_animals:
            return f"{self._Staff__name} feeds {animal.get_name()} the {animal.get_species()}."
        elif animal not in self._Staff__assigned_animals:
            return f"{self._Staff__name} is not assigned to {animal.get_name()}."
        else:
            return "Error!"

    def clean_enclosure(self, enclosure):
        if enclosure in self._Staff__assigned_enclosures:
            enclosure._Enclosure__cleanliness_level = 100
            return f"{self._Staff__name} cleaned the {enclosure._Enclosure__habitat_type} enclosure."
        elif enclosure not in self._Staff__assigned_enclosures:
            return f"{self._Staff__name} is not assigned to {enclosure._Enclosure__habitat_type} enclosure."
        else:
            return "Error!"


class Veterinarian(Staff):
    def __init__(self, name):
        super().__init__(name, "Veterinarian")

    def health_check(self, animal):
        if animal in self._Staff__assigned_animals:
            return f"{self._Staff__name} performed a health check on {animal.get_name()} the {animal.get_species()}."
        elif animal not in self._Staff__assigned_animals:
            return f"{self._Staff__name} is not assigned to {animal.get_name()}."
        else:
            return "Error!"
