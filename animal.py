'''
File: animal.py
Description: A brief description of this Python module.
Author: Shahab Moradi
ID: 1104436331
Username: morsy065
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Animal:
    def __init__(self, name, species, age, diet, sex):
        self._name = name
        self._species = species
        self._age = age
        self._diet = diet
        self._sex = sex

    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age
    
    def get_species(self):
        return self._species
    
    def get_diet(self):
        return self._diet
    
    def get_sex(self):
        return self._sex

class Mammal(Animal):
    def __init__(self, name, species, age, diet, sex):
        super().__init__(name, species, age, diet, sex)


class Lion(Mammal):
    def __init__(self, name, age):
        super().__init__(name, "Lion", age, "Carnivore", "Male")

    def roar(self):
        return f"{self._name} the {self._species} makes a loud ROARR!"
    
    def pouncing(self):
        return f"{self._name} the {self._species} pounces around."
    
    def hunt(self):
        return f"{self._name} the {self._species} stalks the visitors."
    
    def desc(self):
        return f" Name: {self._name} \n Species: {self._species} \n Age: {self._age} \n Dietary Needs: {self._diet} \n Sex: {self._sex}"
    
class Giraffe(Mammal):
    def __init__(self, name, age):
        super().__init__(name, "Giraffe", age, "Herbivore", "Female")

    def eats(self):
        return f"{self._name} the {self._species} reaches for the tree."
    
    def sleeps(self):
        return f"{self._name} the {self._species} sits down to sleep."
    
    def feeds(self):
        return f"{self._name} the {self._species} feeds her kid."
    
    def desc(self):
        return f" Name: {self._name} \n Species: {self._species} \n Age: {self._age} \n Dietary Needs: {self._diet} \n Sex: {self._sex}"
    
class Elephant(Mammal):
    def __init__(self, name, age):
        super().__init__(name, "Elephant", age, "Herbivore", "Male")

    def trumpet(self):
        return f"{self._name} the {self._species} blows his trunk"
    
    def spray(self):
        return f"{self._name} the {self._species} sprays water around."
    
    def reach(self):
        return f"{self._name} the {self._species} reaches for thr visitors with its trunk."
    
    def desc(self):
        return f" Name: {self._name} \n Species: {self._species} \n Age: {self._age} \n Dietary Needs: {self._diet} \n Sex: {self._sex}"
    

Leo = Lion("Leo", 6)
print(Leo.desc())