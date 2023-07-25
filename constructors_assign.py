
'''
Below are my blocks of code showing class, methods,objects and properties.

'''



# no.1
# This is a class Employee.
class Employee:
    def __init__(self,employee_id,name,position,salary):#This is a method.
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary
    def work(self): # this is an overloaded method.
        print(f"{self.name} is {self.position} and earns Shs.{self.salary}")
#Here am giving values to the properties of objects in class Employee.
employee2 = Employee("Staff member", "Husein","Cleaner",60000)
employee3 = Employee("staff member","Hanah","Cook",100000)
employee4 = Employee("staff member","David","Driver",120000)
employee5 = Employee("staff member","John","Assistant Manager",200000)
#Here am calling objects to print out information in method work.
employee2.work()
employee3.work()
employee3.work()
employee5.work()




# no.2
# This is a class Customer.
class Customer:
    def __init__(self,customer_id,name,email,address):#This is a method.
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.address = address
    def get_customer(self): # this is an overloaded method.
        print(f"{self.name} with id number {self.customer_id} lives in {self.address}.")
#Here am giving values to the properties of objects in class Customer.
customer2 = Customer("customer002","Tonny","Tonny002@gmail.com","Kampala")
customer3 = Customer("customer003","Kiwanuka","kiwanuka003@gmail.com","wakiso")
customer4 = Customer("customer004","Noah","Noah004@gmail.com","Kakiri")
customer5 = Customer("customer005", "Shavin","shavin005@gmail.com","Kireka")
#Here am calling objects to print out information in method get_customer.
customer2.get_customer()
customer3.get_customer()
customer4.get_customer()
customer5.get_customer()


#no.3
# This is a class Restaurant.
class Restaurant:
    def __init__(self,name,address,cuisine,rating):   #This is a method.
        self.name = name
        self.address = address
        self.cuisine = cuisine
        self.rating = rating
    def rest(self): # this is an overloaded method.
        print(f"{self.name} in {self.address} serves the best {self.cuisine}.")
 #Here am giving values to the properties of objects in class Restaurant.
restaurant2 = Restaurant("Enro hotel","Mityana","Local food","Three stars")
restaurant3 = Restaurant("Eden hotel","Nsambya","local food","Three stars")
restaurant4 = Restaurant("Luwombo hotel","kireka", "Local food","Four stars")
restaurant5 = Restaurant("London Bridge","FortPortal","Chinese food","five stars")
#Here am calling objects to print out information in method rest.
restaurant2.rest()
restaurant3.rest()
restaurant4.rest()
restaurant5.rest()





#no.4
# This is a class Movie.
class Movie:
    def __init__(self,title,director,genre):#This is a method.
        self.title = title
        self.director = director
        self.genre = genre

    def movies(self):     # this is an overloaded method.
        print(f"{self.title} was directed by {self.director} and it was a {self.genre}.")
#Here am giving values to the properties of objects in class Movie.
movie2 = Movie("Hard Target","Jack Bucket","Action Movie")
movie3 = Movie("Die Hard","Jack Boehner","Action Movie")
movie4 = Movie( "Megan","Jenny Green","Sci-Fi Movie")
movie5 = Movie("Twins","Jane Doe","Horror Movie")
#Here am calling objects to print out information in method movies.
movie2.movies() 
movie3.movies()
movie4.movies()
movie5.movies() 


#no.5
# This is a class Course.
class Course:
    def __init__(self,name,instructor,student):#This is a method.
        self.name = name
        self.instructor = instructor
        self.student = student
    def educ(self): # this is an overloaded method.
        print(f"{self.name} is taught by {self.instructor} to a student known as {self.student}.")
#Here am giving values to the properties of objects in class Course.
course2 = Course("Block chain","MR.kakungulu Emmanuel","Kigozi Farouq")
course3 = Course( "Criminal Law","Mr.Mawejje Patrick","Ssebunya Ibrahim")
course4 = Course("Civil Engineering","Mrs.Nabbongo Betty","Nakimuli Claire") 
course5 = Course( "Medicine","MR.Kasozi Mike","Kigozi Farouq")
#Here am calling objects to print out information in method educ.
course2.educ()
course3.educ()
course4.educ()
course5.educ()

#no.6
# This is a class School.
class School:
    def __init__(self,name,address,principal):#This is a method.
        self.name = name
        self.address = address
        self.principal = principal
    def sch(self): # this is an overloaded method.
        print(f"{self.name} is located in {self.address} and headed by {self.principal}.")

#Here am giving values to the properties of objects in class School.
school2 = School( "London college","Nansana","Katongole Leonard")
school3 = School("Riverdale Preparatory School","Kyebando","Faith Komugisha")
school4 = School("Cambridge International School","Munyonyo","Cornerstone Divinci")
school5 = School("Kings way High School","Entebbe","Ssentongo Lordes")
#Here am calling objects to print out information in method 
school2.sch() 
school3.sch() 
school4.sch() 
school5.sch() 


#no.7
# This is a class Box.
class Box:
    def __init__(self,width,height,color):#This is a method.
        self.width = width
        self.height = height
        self.color = color
    def boxes(self): # this is an overloaded method.
        print(f"I have an {self.color} rectangular box with width {self.width} and height {self.height}.")
#Here am giving values to the properties of objects in class Box.
rectanglebox2 = Box("5cm","4cm", "green")
rectanglebox3 = Box("6cm","5cm","purle")
rectanglebox4 = Box("7cm","12cm","blue") 
rectanglebox5 = Box("7cm","14cm","orange")
#Here am calling objects to print out information in method boxes.
rectanglebox2.boxes()
rectanglebox3.boxes()
rectanglebox4.boxes()
rectanglebox5.boxes()



#no.8
# This is a class Poduct.
class Product:
    def __init__(self,name,price,description):#This is a method.
        self.name = name
        self.price = price
        self.description = description
    def prdt(self): # this is an overloaded method.
        print(f"{self.name} are sold at {self.price} because they are {self.description}.")
#Here am giving values to the properties of objects in class Product.
product2 = Product("Televisions","shs.1,500,000", "Fragile")
product3 = Product("Fridges","shs.1,500,000", "Fragile")
product4 = Product("Hand bags","shs.15000","Not Fragile")
product5 = Product("Cups","shs.50000","fragile")
 #Here am calling objects to print out information in method prdt.
product2.prdt()
product3.prdt()
product4.prdt()
product5.prdt()



#no.9
# This is a class Bank.
class Bank:
    def __init__(self, name,branch,location):#This is a method.
        self.name = name
        self.branch = branch
        self.location = location
    def banks(self): # this is an overloaded method.
        print(f"{ self.name } , { self.branch } located at { self.location} provides good services.")
#Here am giving values to the properties of objects in class Bank.
bank2 = Bank("DFCU bank","Kampala branch", "Wandegeya")
bank3 = Bank("Stanbic bank","Kampala branch","Katikamu")
bank4 = Bank("Absa bank","Kampala branch","Wakiso")
bank5 = Bank("Cairo bank","Kampala branch","Kiwatule")
#Here am calling objects to print out information in method banks.
bank2.banks()
bank3.banks()
bank4.banks()
bank5.banks()




#no.10
# This is a class Song.
class Song:
    def __init__(self,title,artist,duration):#This is a method.
        self.title = title
        self.artist = artist
        self.duration = duration
    def songs(self): # this is an overloaded method.
        print(f"{self.artist} sang a song called {self.title} and it runs for {self.duration}.")
    #Here am giving values to the properties of objects in class Song.
song2 = Song("My heart","Serena Gomez","3 minutes")
song3 = Song("Sitya danger","Alien skin","3.5 minutes")
song4 = Song("Favourite song","Toosi","2.9 minutes")
song5 = Song("So low","Remmy boys","4 minutes")
#Here am calling objects to print out information in method songs.
song2.songs()
song3.songs()
song4.songs()
song5.songs()
