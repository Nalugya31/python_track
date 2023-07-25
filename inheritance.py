'''
Methods in the different class can be shared.
Piece of code demostrates inheritance, 
where class Dog inherits(take on properties) from from class Animal.
Class Dog and Snake are not relatable to one other 
but they inherit from class Animal.
if the methods inherite from each other, they the output is the same in the terminal.
Overiding is where we use the same variable or property to output two or more values.
and a snake can inherit from a dog and a dog can inherit from a snake.(multiple inheritance)
'''


class Animal: # class
    name ="" 
    family = ""
    gender = ""

class Dog(Animal):# inheritated class Animal.(accessing the properties of Animal)
    sound = "barking" # they dont share sounds because they are different.
    def investigate(self): 
        print(f"{self.name} sniffs to investigate.")


class Cow(Animal):# inheritated class Animal.(accessing the properties of Animal)
    sound = "mooos" # if you comment out this then the sound you get is for the dog if you happen to call sound cow.
    color = "black"
    def use(self):
        print(f"{self.name} is a domestic animal.")

# lets instantiate the objects of class Dog.
gshephard = Dog()
gshephard.name = "Freddy"
gshephard.family = "looki"
gshephard.gender = "male"
print(f"{gshephard.sound}")



# lets instantiate the objects of class Dog.
ox = Cow()
ox.name = "Zebu"
ox.gender = "female"
ox.family = "domestic"
print(f"{ox.sound}") # now this is overriding the sound of the dog.
print(f"{ox.color}")



