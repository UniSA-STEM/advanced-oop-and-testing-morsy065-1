'''
File: animal.py
Description: A brief description of this Python module.
Author: Shahab Moradi
ID: 1104436331
Username: morsy065
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Animal:
    def __init__(self, name, age, species, diet, sex):
        self.__name = name
        self.__age = age
        self.__species = species
        self.__diet = diet
        self.__sex = sex

    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def get_species(self):
        return self.__species
    
    def get_diet(self):
        return self.__diet
    
    def get_sex(self):
        return self.__sex
    
    def method(self):
        s

class Mammal(Animal):
    def __init__(self, name, age, species, dietary_needs, sex):
        super().__init__(name, age, species, dietary_needs, sex)


class Lion(Mammal):
    def __init__(self, name, age):
        super().__init__(name, age, "Lion", "Carnivore", "Male")