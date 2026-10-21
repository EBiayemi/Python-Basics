class Family:
    def __init__(self, eye_color, hair_color):
        self.eye_color = eye_color
        self.hair_color = hair_color
    def show_traits(self):
        print("Eye color:", self.eye_color)
        print("Hair color:", self.hair_color)
class Child(Family):
    def __init__(self, eye_color, hair_color, favorite_color):
        super().__init__(eye_color, hair_color)
        self.favorite_color = favorite_color
    def show_traits(self):
        super().show_traits()
        print("Favorite color:", self.favorite_color)
my_family = Family("Brown", "Black")
me = Child("Brown", "Black", "Blue")
my_family.show_traits()
print()
me.show_traits()
print(issubclass(Child, Family))