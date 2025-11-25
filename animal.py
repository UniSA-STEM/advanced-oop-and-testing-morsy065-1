'''
File: animal.py
Description: A brief description of this Python module.
Author: Shahab Moradi
ID: 1104436331
Username: morsy065
This is my own work as defined by the University's Academic Integrity Policy.
'''
# Animal class which is the parent class.
class Animal:
    def __init__(self, name, species, age, diet, sex):
        self._name = name
        self._species = species
        self._age = age
        self._diet = diet
        self._sex = sex
    # getters for the Animal class attributes
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
# The Mammal class which inherits the Animal class' attributes
class Mammal(Animal):
    def __init__(self, name, species, age, diet, sex):
        super().__init__(name, species, age, diet, sex)
# The species classes that belong the Mammal group
class Lion(Mammal):
    def __init__(self, name, age):
        super().__init__(name, "Lion", age, "Carnivore", "Male")
    # basic action methods
    def roar(self):
        return f"{self._name} the {self._species} makes a loud ROARR!"
    
    def pouncing(self):
        return f"{self._name} the {self._species} pounces around."
    
    def hunt(self):
        return f"{self._name} the {self._species} stalks the visitors."
    # This method list down the description for each specie.
    def desc(self):
        return f" Name: {self._name} \n Species: {self._species} \n Age: {self._age} \n Dietary Needs: {self._diet} \n Sex: {self._sex} \n -----------"
    
class Giraffe(Mammal):
    def __init__(self, name, age):
        super().__init__(name, "Giraffe", age, "Herbivore", "Female")
    # basic action methods
    def eats(self):
        return f"{self._name} the {self._species} reaches for the tree."
    
    def sleeps(self):
        return f"{self._name} the {self._species} sits down to sleep."
    
    def feeds(self):
        return f"{self._name} the {self._species} feeds her kid."
    
    def desc(self):
        return f" Name: {self._name} \n Species: {self._species} \n Age: {self._age} \n Dietary Needs: {self._diet} \n Sex: {self._sex} \n -----------"
    
class Elephant(Mammal):
    def __init__(self, name, age):
        super().__init__(name, "Elephant", age, "Herbivore", "Male")
    # basic action methods
    def trumpet(self):
        return f"{self._name} the {self._species} blows his trunk"
    
    def spray(self):
        return f"{self._name} the {self._species} sprays water around."
    
    def reach(self):
        return f"{self._name} the {self._species} reaches for thr visitors with its trunk."
    
    def desc(self):
        return f" Name: {self._name} \n Species: {self._species} \n Age: {self._age} \n Dietary Needs: {self._diet} \n Sex: {self._sex} \n -----------"
# The Bird Class which inherits the Animal class' attributes
class Bird(Animal):
    def __init__(self, name, species, age, diet, sex):
        super().__init__(name, species, age, diet, sex)
# The bird species and their functions
class Parrot(Bird):
    def __init__(self, name, age):
        super().__init__(name, 'Parrot', age, 'Omnivore', 'Male')
    # basic action methods
    def talk(self, word):
        return f"{self._name} the {self._species} starts yelling {word}."
    
    def nest(self):
        return f"{self._name} the {self._species} flies back to its nest."
    
    def scream(self):
        return f"{self._name} the {self._species} screams for no reason!"
    
    def desc(self):
        return f" Name: {self._name} \n Species: {self._species} \n Age: {self._age} \n Dietary Needs: {self._diet} \n Sex: {self._sex} \n -----------"
    
class Penguin(Bird):
    def __init__(self, name, age):
        super().__init__(name, 'Penguin', age, 'Carnivore', 'Female')
    # basic action methods
    def waddle(self):
        return f"{self._name} the {self._species} waddles across its habitat."
    
    def swim(self):
        return f"{self._name} the {self._species} dives in the water for a swim."
    
    def follow(self):
        return f"{self._name} the {self._species} follows the zookeeper."

    def desc(self):
        return f" Name: {self._name} \n Species: {self._species} \n Age: {self._age} \n Dietary Needs: {self._diet} \n Sex: {self._sex} \n -----------"
# The Reptile class 
class Reptile(Animal):
    def __init__(self, name, species, age, diet, sex):
        super().__init__(name, species, age, diet, sex)

class Snake(Reptile):
    def __init__(self, name, age):
        super().__init__(name, 'Snake', age, 'Carnivore', 'Male')
    # basic action methods
    def hss(self):
        return f"{self._name} the {self._species} starts to hssssss."
    
    def sleep(self):
        return f"{self._name} the {self._species} coils its body to sleep."
    
    def desc(self):
        return f" Name: {self._name} \n Species: {self._species} \n Age: {self._age} \n Dietary Needs: {self._diet} \n Sex: {self._sex} \n -----------"
    
class Crocodile(Reptile):
    def __init__(self, name, age):
        super().__init__(name, 'Crocodile', age, 'Carnivore', 'Male')
    # basic action methods
    def lurking(self):
        return f"{self._name} the {self._species} lurks around its swamp."
    
    def sun_bath(self):
        return f"{self._name} the {self._species} baths in the sun."
    
    def desc(self):
        return f" Name: {self._name} \n Species: {self._species} \n Age: {self._age} \n Dietary Needs: {self._diet} \n Sex: {self._sex} \n -----------"
