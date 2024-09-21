class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    __all = []  # Private class variable to store all instances of Pet

    def __init__(self, name: str, pet_type: str, owner=None):
        if pet_type not in self.PET_TYPES:
            raise ValueError(f"Invalid pet type: {pet_type}. Must be one of {self.PET_TYPES}.")
        
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        
        # Add this pet instance to the all list
        Pet.__all.append(self)

    @classmethod
    def get_all(cls):
        """Return all instances of Pet."""
        return cls.__all

    def __str__(self) -> str:
        return f"{self.pet_type.capitalize()} named {self.name}"

    def __repr__(self) -> str:
        return f"Pet(name={self.name}, pet_type={self.pet_type})"

class Owner:
    def __init__(self, name: str):
        self.name = name
        self._pets = []  # Private list to hold pets

    def pets(self) -> list:
        """Returns a full list of the owner's pets."""
        return self._pets

    def add_pet(self, pet: Pet):
        """Adds a pet to the owner, ensuring it is of type Pet."""
        if not isinstance(pet, Pet):
            raise TypeError("pet must be an instance of Pet.")
        
        if pet.owner is not None:
            raise Exception(f"{pet.name} already has an owner.")
        
        self._pets.append(pet)
        pet.owner = self  # Set the pet's owner

    def get_sorted_pets(self) -> list:
        """Returns a sorted list of pets by their names."""
        return sorted(self._pets, key=lambda p: p.name)

    def __str__(self) -> str:
        return f"Owner: {self.name}, Pets: {[pet.name for pet in self._pets]}"

    def __repr__(self) -> str:
        return f"Owner(name={self.name}, pets={self._pets})"


# Example usage and tests remain unchanged
if __name__ == "__main__":
    try:
        owner1 = Owner("Alice")
        owner2 = Owner("Bob")

        pet1 = Pet("Fido", "dog")
        pet2 = Pet("Whiskers", "cat")
        pet3 = Pet("Polly", "bird")

        owner1.add_pet(pet1)
        owner1.add_pet(pet2)
        owner2.add_pet(pet3)

        print(owner1)  # Owner: Alice, Pets: ['Fido', 'Whiskers']
        print(owner2)  # Owner: Bob, Pets: ['Polly']

        # Display sorted pets
        print("Sorted pets of Alice:", owner1.get_sorted_pets())

    except Exception as e:
        print(e)
