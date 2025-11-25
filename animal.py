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
    def __init__(self, name, species, age, diet, type):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__diet = diet
        self.__type = type
    # getters for the Animal class attributes
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_species(self):
        return self.__species

    def get_diet(self):
        return self.__diet

    def get_type(self):
        return self.__type
    
    def make_sound(self):
        pass

    def desc(self):
        pass
# The Mammal class which inherits the Animal class' attributes
class Mammal(Animal):
    def __init__(self, name, species, age, diet, type):
        super().__init__(name, species, age, diet, type)
        
# The species classes that belong the Mammal group
class Lion(Mammal):
    def __init__(self, name, age):
        super().__init__(name, "Lion", age, "Carnivore", "Savannah")
    # basic action methods
    def roar(self):
        return f"{self._Animal__name} the {self._Animal__species} makes a loud ROARR!"
    
    def pouncing(self, enclosure):
        enclosure._Enclosure__cleanliness_level -= 5
        return f"{self._Animal__name} the {self._Animal__species} pounces around."
    
    def hunt(self):
        return f"{self._Animal__name} the {self._Animal__species} stalks the visitors."
    # This method list down the description for each specie.
    def desc(self):
        return f" ----------- \n Name: {self._Animal__name} \n Species: {self._Animal__species} \n Age: {self._Animal__age} \n Dietary Needs: {self._Animal__diet} \n type: {self._Animal__type} \n -----------"
    
class Giraffe(Mammal):
    def __init__(self, name, age):
        super().__init__(name, "Giraffe", age, "Herbivore", "Savannah")
    # basic action methods
    def eats(self, enclosure):
        enclosure._Enclosure__cleanliness_level - 3
        return f"{self._Animal__name} the {self._Animal__species} reaches for the tree."
    
    def sleeps(self):
        return f"{self._Animal__name} the {self._Animal__species} sits down to sleep."
    
    def feeds(self, enclosure):
        enclosure._Enclosure__cleanliness_level -= 1
        return f"{self._Animal__name} the {self._Animal__species} feeds her kid."
    
    def desc(self):
        return f" ----------- \n Name: {self._Animal__name} \n Species: {self._Animal__species} \n Age: {self._Animal__age} \n Dietary Needs: {self._Animal__diet} \n type: {self._Animal__type} \n -----------"
    
class Elephant(Mammal):
    def __init__(self, name, age):
        super().__init__(name, "Elephant", age, "Herbivore", "Savannah")
    # basic action methods
    def trumpet(self):
        return f"{self._Animal__name} the {self._Animal__species} blows his trunk"
    
    def spray(self, enclosure):
        enclosure._Enclosure__cleanliness_level - 11
        return f"{self._Animal__name} the {self._Animal__species} sprays water around."
    
    def reach(self, enclosure):
        enclosure._Enclosure__cleanliness_level - 2
        return f"{self._Animal__name} the {self._Animal__species} reaches for thr visitors with its trunk."
    
    def desc(self):
        return f" ----------- \n Name: {self._Animal__name} \n Species: {self._Animal__species} \n Age: {self._Animal__age} \n Dietary Needs: {self._Animal__diet} \n type: {self._Animal__type} \n -----------"
# The Bird Class which inherits the Animal class' attributes
class Bird(Animal):
    def __init__(self, name, species, age, diet, type):
        super().__init__(name, species, age, diet, type)
# The bird species and their functions
class Parrot(Bird):
    def __init__(self, name, age):
        super().__init__(name, 'Parrot', age, 'Omnivore', 'Forest')
    # basic action methods
    def talk(self, word):
        return f"{self._Animal__name} the {self._Animal__species} starts yelling {word}."
    
    def nest(self, enclosure):
        enclosure._Enclosure__cleanliness_level - 1
        return f"{self._Animal__name} the {self._Animal__species} flies back to its nest."
    
    def scream(self):
        return f"{self._Animal__name} the {self._Animal__species} screams for no reason!"
    
    def desc(self):
        return f" ----------- \n Name: {self._Animal__name} \n Species: {self._Animal__species} \n Age: {self._Animal__age} \n Dietary Needs: {self._Animal__diet} \n type: {self._Animal__type} \n -----------"
    
class Penguin(Bird):
    def __init__(self, name, age):
        super().__init__(name, 'Penguin', age, 'Carnivore', 'Aquatic')
    # basic action methods
    def waddle(self, enclosure):
        enclosure._Enclosure__cleanliness_level - 2
        return f"{self._Animal__name} the {self._Animal__species} waddles across its habitat."
    
    def swim(self, enclosure):
        enclosure._Enclosure__cleanliness_level - 3
        return f"{self._Animal__name} the {self._Animal__species} dives in the water for a swim."
    
    def follow(self, enclosure):
        enclosure._Enclosure__cleanliness_level - 1
        return f"{self._Animal__name} the {self._Animal__species} follows the zookeeper."

    def desc(self):
        return f" ----------- \n Name: {self._Animal__name} \n Species: {self._Animal__species} \n Age: {self._Animal__age} \n Dietary Needs: {self._Animal__diet} \n type: {self._Animal__type} \n -----------"
# The Reptile class 
class Reptile(Animal):
    def __init__(self, name, species, age, diet, type):
        super().__init__(name, species, age, diet, type)

class Snake(Reptile):
    def __init__(self, name, age):
        super().__init__(name, 'Snake', age, 'Carnivore', 'Forest')
    # basic action methods
    def hss(self):
        return f"{self._Animal__name} the {self._Animal__species} starts to hssssss."
    
    def sleep(self):
        return f"{self._Animal__name} the {self._Animal__species} coils its body to sleep."
    
    def desc(self):
        return f" ----------- \n Name: {self._Animal__name} \n Species: {self._Animal__species} \n Age: {self._Animal__age} \n Dietary Needs: {self._Animal__diet} \n type: {self._Animal__type} \n -----------"
    
class Crocodile(Reptile):
    def __init__(self, name, age):
        super().__init__(name, 'Crocodile', age, 'Carnivore', 'Aquatic')
    # basic action methods
    def lurking(self):
        return f"{self._Animal__name} the {self._Animal__species} lurks around its swamp."
    
    def sun_bath(self):
        return f"{self._Animal__name} the {self._Animal__species} baths in the sun."
    
    def desc(self):
        return f" ----------- \n Name: {self._Animal__name} \n Species: {self._Animal__species} \n Age: {self._Animal__age} \n Dietary Needs: {self._Animal__diet} \n type: {self._Animal__type} \n -----------"