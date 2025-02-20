## R. Alvarez, 2025
## Python bootcamp


from animals import Animal, Dog, Cat

class Human:

    owners_counter = 0
    owners = {}

    def __init__(self, name, last_name, gender, age, city, email, zip_code, pets=None):
        self.name = name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.city = city
        self.email = email
        self.zip_code = zip_code
        self.pets = pets if pets is not None else []
        Human.owners_counter += 1
        Human.owners[name.lower().strip()] = self

    def pet_register (self, name, color, species, eyes, weight, age, **kwargs):
        if (species.lower() == "dog"):
            new_pet = Dog (self, name, color, species, eyes, weight, age, **kwargs)
            self.pets.append(new_pet)
        else:
            new_pet = Cat (self, name, color, species, eyes, weight, age, **kwargs)
            self.pets.append(new_pet)

