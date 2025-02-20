## R. Alvarez, 2025
## Python bootcamp


class Animal:

    dog_counter = 0
    cat_counter = 0
    dog_transfers = 0
    cat_transfers = 0

    registered_animals = []

# Constructor Animal

    def __init__(self, owner, name, color, species, eyes, weight, age):
        self.owner = owner
        self.name = name
        self.color = color
        self.species = species
        self.eyes = eyes
        self.weight = weight
        self.age = age

# Métodos Animal

    def sleep (self, hours):
        pass
        return self

    def eat (self, food, quantity):
        pass
        return self

    def run (self, distance, terrain):
        pass
        return self

    def play (self, minutes, place):
        pass
        return self

# Constructor Dog

class Dog(Animal):

    def __init__(self, owner, name, color, species, eyes, weight, age, breed, animality, children=True, city_ID=""):
        super().__init__(owner, name, color, species, eyes, weight, age)
        self.breed = breed
        self.animality = animality
        self.children = children
        if (city_ID == ""):
            self.city_ID = f"CityXYZ_Dog_202500{Animal.dog_counter + 1}"
            Animal.dog_counter += 1
        else:
            self.city_ID = city_ID
            Animal.dog_transfers += 1
        Animal.registered_animals.append (self)

# Constructor Cat

class Cat(Animal):

    def __init__(self, owner, name, color, species, eyes, weight, age, petability, felv=False, city_ID=""):
        super().__init__(owner, name, color, species, eyes, weight, age)
        self.felv = felv
        self.petability = petability
        if (city_ID == ""):
            self.city_ID = f"CityXYZ_Cat_202500{Animal.cat_counter + 1}"
            Animal.cat_counter += 1
        else:
            self.city_ID = city_ID
            Animal.cat_transfers += 1
        Animal.registered_animals.append (self)

