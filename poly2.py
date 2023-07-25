class Cat:# this  is class Cat.
    def __init__(self, name, age):# this is a shish method.
        self.name = name# these are properties
        self.age = age

    def info(self):# this is a method.
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):# this is a method.
        print("Meow")# this is a behaviour



class Dog:# this is class Dog
    def __init__(self, name, age):# this is a shish method.
        self.name = name  # these are properties
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")
#inheritanting method make_sound from class Cat.
    def make_sound(self):
        print("Bark")# this is a behaviour

# here we are instantiating the objects of class Dog and Class Cat.
cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)
# we are using the for loop to iterate over the two classes with their objects
# to print out their behaviour.
for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()

