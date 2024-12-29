class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []

    def __init__(self, name, pet_type, owner=''):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.check_pettype(pet_type)
        self.add_pet(self)

    @classmethod
    def check_pettype(cls, pet_type):
        if pet_type in cls.PET_TYPES:
            return True
        else: 
            raise TypeError('pet_type is one of the types of pets in PET_TYPES')
        
    @classmethod
    def add_pet(cls, self):
        cls.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if isinstance (pet, Pet):
            pet.owner = self
        else:
            raise TypeError('pet must be an instance of Pet')
        
    def get_sorted_pets(self, key=lambda pet: pet.name):
       
        return sorted(self.pets(), key=key)