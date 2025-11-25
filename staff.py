'''
File: staff.py
Description: A brief description of this Python module.
Author: Shahab Moradi
ID: 1104436331
Username: morsy065
This is my own work as defined by the University's Academic Integrity Policy.
'''
# Staff class with getters
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
    # this assigns the animal chosen to the chosen staff member
    def assign_animal(self, animal):
        self.__assigned_animals.append(animal)
        return f"{animal.get_name()} ({animal.get_species()}) assigned to {self.__name}."
    # this assigns an enclosure to the chosen staff
    def assign_enclosure(self, enclosure):
        self.__assigned_enclosures.append(enclosure)
        return f"{enclosure._Enclosure__habitat_type} enclosure assigned to {self.__name}."
    # this shows a list of animals assigned to the staff
    def list_animals(self):
        if not self.__assigned_animals:
            return f"{self.__name} has no assigned animals."
        elif self.__assigned_animals:
            return [f"{animal.get_name()} ({animal.get_species()})" for animal in self.__assigned_animals]
        else:
            return "Error!"
    # this shows a list of enclosures assigned to the staff
    def list_enclosures(self):
        if not self.__assigned_enclosures:
            return f"{self._name} has no assigned enclosures."
        elif self.__assigned_enclosures:
            return [f"{enclosure._Enclosure__habitat_type} (Size: {enclosure._Enclosure__size} m²)" for enclosure in self.__assigned_enclosures]
        else:
            return "Error!"

# Zookeeper class which inherits the Staff class
class Zookeeper(Staff):
    def __init__(self, name):
        super().__init__(name, "Zookeeper")
    # this allows the zookep to feed the animals assigned to it and show a message if the animal is not assigned to the zookeeper
    def feed_animal(self, animal):
        if animal in self._Staff__assigned_animals:
            return f"{self._Staff__name} feeds {animal.get_name()} the {animal.get_species()}."
        elif animal not in self._Staff__assigned_animals:
            return f"{self._Staff__name} is not assigned to {animal.get_name()}."
        else: # this is prints a error incase anything odd is entered
            return "Error!"
    # this lets the zookeeper clean the enclosure if its assigned to it
    def clean_enclosure(self, enclosure):
        if enclosure in self._Staff__assigned_enclosures:
            enclosure._Enclosure__cleanliness_level = 100
            return f"{self._Staff__name} cleaned the {enclosure._Enclosure__habitat_type} enclosure."
        elif enclosure not in self._Staff__assigned_enclosures:
            return f"{self._Staff__name} is not assigned to {enclosure._Enclosure__habitat_type} enclosure."
        else:
            return "Error!"

# this class also inherits the Staff class
class Veterinarian(Staff):
    def __init__(self, name):
        super().__init__(name, "Veterinarian")
    # this performs a health check on the animals the veterinarian is assigned to
    def health_check(self, animal):
        if animal in self._Staff__assigned_animals:
            return f"{self._Staff__name} performed a health check on {animal.get_name()} the {animal.get_species()}."
        elif animal not in self._Staff__assigned_animals:
            return f"{self._Staff__name} is not assigned to {animal.get_name()}."
        else:
            return "Error!"
