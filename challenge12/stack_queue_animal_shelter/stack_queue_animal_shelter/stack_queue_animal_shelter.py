class AnimalShelter:

    def __init__(self):
        self.dogs = []
        self.cats = []

    def enqueue(self, animal):
        if animal.species == "dog":
            self.dogs.append(animal)
        elif animal.species == "cat":
            self.cats.append(animal)
        else:
            raise ValueError("Invalid animal species")

    def dequeue(self, pref):
        if pref == "dog":
            if len(self.dogs) == 0:
                return None
            else:
                return self.dogs.pop(0)
        elif pref == "cat":
            if len(self.cats) == 0:
                return None
            else:
                return self.cats.pop(0)
        else:
            raise ValueError("Invalid preference")