## R. Alvarez, 2025
## Python bootcamp


from animals import Animal, Dog, Cat
from humans import Human

class Registro:

    def pet_data_entry ():
        print ()
        print ("***********************************")
        print ("Enter your pet's information below")
        name = input ("Name: ")
        color = input ("Color: ")
        species = input ("Species: ")
        eyes = input ("Eyes: ")
        weight = input ("Weight: ")
        age = input ("Age :")
        if (species.lower() == "dog"):
            breed = input ("Breed: ")
            animality = input ("Animality: ")
            children = input ("Goes well with childfen (yes/no)? ")
            city_ID = input ("Registration code (keep empty if your pet is not registered yet): ")
            return (name, color, species, eyes, weight, age, breed, animality, children, city_ID)
        elif (species.lower() == "cat"):
            felv = input ("Positive for fiv/felv (yes/no): ")
            petability = input ("Stays close and interacts with humans (yes/no)?")
            city_ID = input ("Registration code (keep empty if your pet is not registered yet): ")
            return (name, color, species, eyes, weight, age, felv, petability, city_ID)
        else:
            print ("*********************************************************************************")
            print ("Your pet cannot be registered. The municipality only registers <dogs> and <cats>.")
            print ("Stay away from CityXYZ.")
            print ("Go away with your beast.")
            print ()
            return (None)

    def request_registry():
        pet = Registro.pet_data_entry()
        name = ""
        print ()
        print ("Informe quem é o dono do pet conforme as alternativas abaixo -------------")
        for value in Human.owners:
            print (value)
        while name not in Human.owners:
            name = input ("Quem e o dono do pet? ").strip().lower()
        owner = Human.owners.get(name, None)
        if (pet[2].lower()=="dog"):
            owner.pet_register(pet[0], pet[1], pet[2], pet[3], pet[4], pet[5], breed=pet[6], animality=pet[7], children=pet[8], city_ID=pet[9])
        else:
            owner.pet_register(pet[0], pet[1], pet[2], pet[3], pet[4], pet[5], felv=pet[6], petability=pet[7], city_ID=pet[8])
        return (owner)
    
    def show_pet_owner(owner):
        print ("********************")
        print (f"{owner.name} {owner.last_name} from {owner.city} owns the following pets:")
        i = 0
        for pet in owner.pets:
            print (f"Pet name: {owner.pets[i].name}")
            print (f"Pet species: {owner.pets[i].species}")
            print (f"Pet color: {owner.pets[i].color}")
            print (f"Pet eyes: {owner.pets[i].eyes}")
            print (f"Pet weight: {owner.pets[i].weight}")
            print (f"Pet age: {owner.pets[i].age}")
            print (f"City registration code: {owner.pets[i].city_ID}")
            if (owner.pets[i].species == "dog"):
                print (f"Pet 'animality': {owner.pets[i].animality}")
                print (f"Pet breed: {owner.pets[i].breed}")
                print (f"Goes well with children? {owner.pets[i].children}")
                
            else:
                print (f"Likes to interact with humans?: {owner.pets[i].petability}")
                print (f"FELV status: {owner.pets[i].felv}")
            i += 1
        return ()



