'''
Self is a reference that helps us to denote the properties of a class.
pass means ignore. anything below it is not considered
"self" its a reference to its objects' properties and you can change it to anything you want.
The shish method is what we use to declare parameters.
Calling a class is called instantiation like on line 16. 
And this involves the process of giving values to the objects.
A method with __init__ is called a constructor.
A constructor is used to initialize an instantiated object.
'''
class School: # dynamic class
   def __init__(self,name,location,nu_teacher,nu_students,motto): # that helps to create and pass values of a particular object to the properties of a class.
      self.name = name  # (self.name)properties or attributes.= (name)the value.
      self.location = location
      self.nu_teacher = nu_teacher
      self.nu_students = nu_students
      self.motto = motto
   def register(self): # Its overloaded because each object uses it differently.
      print(f"{self.name} is registered fully with UNEB.")

school1 = School("Mase Junior School","Mityana",20,100,"For God and my country") # instantiation
school2 = School("Mumsa","kla",20,100,"For God and my country") # instantiation
school1.register()
school2.register()







class Country:
   def __init__(self,a,b,c):
      self.name = a 
      self.city = b
      self.population = c
   def country(self):
      print(f"{self.city} in {self.name} has {self.population} people")
country1 = Country("Uganda", "Kampala", 50000000)
country1.country()

      
class Continent:
   def __init__(continent,a,b,c):
      continent.name = a
      continent.location = b
      continent.waterbodies = c
   def conti(continent):
      print(f"{continent.name} in {continent.location} has {continent.waterbodies} water bodies.")
conti1 = Continent("Africa", " the south" , 2300)
conti1.conti()
