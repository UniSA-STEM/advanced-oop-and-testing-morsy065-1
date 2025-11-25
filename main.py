'''
File: main.py
Description: A brief description of this Python module.
Author: Shahab Moradi
ID: 1104436331
Username: morsy065
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal, Mammal, Lion, Elephant, Giraffe, Parrot, Penguin, Snake, Crocodile
from enclosure import Enclosure, Savannah, Aquatic, Forest
from staff import Staff, Zookeeper, Veterinarian

# Create animals
simba = Lion("Simba", 5)
dumbo = Elephant("Dumbo", 12)
jack = Giraffe("Jack", 7)
polly = Parrot("Polly", 3)
ping = Penguin("Ping", 4)
snake = Snake("Snake", 2)
croc = Crocodile("Croc", 6)

# Create enclosures
savannah = Savannah(500)
aquatic = Aquatic(300)
forest = Forest(400)

# Add animals to enclosures
print("\n---Adding animals to Enslosures---\n")
print(savannah.add_animal(simba))
print(savannah.add_animal(dumbo))
print(savannah.add_animal(jack))
print(aquatic.add_animal(ping))
print(aquatic.add_animal(croc))
print(forest.add_animal(polly))
print(forest.add_animal(snake))

# Create staff
lisa = Zookeeper("Lisa")
bob = Veterinarian("Bob")

# Assign animals and enclosures
print("\n---Assigning animals and enclosures to staff---\n")
print(lisa.assign_animal(simba))
print(lisa.assign_animal(jack))
print(lisa.assign_enclosure(savannah))

print(bob.assign_animal(dumbo))
print(bob.assign_animal(polly))
print(bob.assign_enclosure(aquatic))
print(bob.assign_enclosure(forest))


# Staff actions
print("\n---Staff feeding etc---\n")
print(lisa.feed_animal(simba))
print(lisa.feed_animal(dumbo))
print(lisa.clean_enclosure(savannah))
print(lisa.clean_enclosure(aquatic))

print(bob.health_check(dumbo))
print(bob.health_check(jack))

# Enclosure statuses after actions
print("\n---Enclosure status'---\n")
print(savannah.status())
print(aquatic.status())
print(forest.status())

# List assigned animals for staff
print("\n---List of staff animals---\n")
print("Lisa's animals:", lisa.list_animals())
print("Lisa's enclosures:", lisa.list_enclosures())
print("Bob's animals:", bob.list_animals())
print("Bob's enclosures:", bob.list_enclosures())