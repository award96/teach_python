# succingtly illustrates the outline of a class

class Puppy:
    def __init__(self, name):
        self.cute = True
        self.name = name
        self.happy = None

    def pet(self):
        print(f"{self.name} is happy! They wag their tail")
        self.happy = True
    
    def get_name(self):
        print("Puppies can't speak!")