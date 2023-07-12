''' 
the name of the class should start with a capital letter.
things in a class are called attributes or properties.
below is a defined class with attributes or properties.
'''
class Girl:
    name = "Jessy" 
    age = 20
    gender = "female"
    size = "small"
    family = "kabaka"
    size_of_bra = "small"

print(Girl.name)
print(Girl.age)
print(Girl.gender)
print(Girl.size)
print(Girl.family)
print(Girl.size_of_bra)

girl2 = Girl()
girl2.name = "Trevin"
girl2.age = 27
girl2.gender = "female"
print(f"{girl2.name} is {girl2.age} years old")# literal strings(strings that represent values.)


girl3 = Girl()
girl3.name = "tinky"
girl3.age = 12 

print(f"{girl3.name} is {girl3.age} years old")


# create 10 classes with 5 corresponding objects.
# and print out atleast one information for each object.
# no.1
class Employee:
    employee_id = "Super admin"
    name = "Hassan"
    position = "Manager"
    salary = 250000

employee2 = Employee()
employee2.employee_id = "Staff member"
employee2.name = "Husein"
employee2.position = "Cleaner"
employee2.salary = 60000

employee3 = Employee()
employee3.employee_id = "staff member"
employee3.name = "Hanah"
employee3.position = "Cook"
employee3.salary = 100000

employee4 = Employee()
employee4.employee_id = "staff member"
employee4.name = "David"
employee4.position = "Driver"
employee4.salary = 120000


employee5 = Employee()
employee5.employee_id = "staff member"
employee5.name = "John"
employee5.position = "Assistant Manager"
employee5.salary = 200000
print(f"{employee3.name} is {employee3.position} and earns Shs.{employee3.salary}")

# no.2
class Customer:

    customer_id = "customer001"
    name = "Gloria"
    email = "gloria@gmail.com"
    address = "Mityana"

customer2 = Customer()
customer2.customer_id = "customer002"
customer2.name = "Tonny"
customer2.email = "Tonny002@gmail.com"
customer2.address = "Kampala"

customer3 = Customer()
customer3.customer_id = "customer003"
customer3.name = "Kiwanuka"
customer3.email = "kiwanuka003@gmail.com"
customer3.address = "Kampala"

customer4 = Customer()
customer4.customer_id = "customer004"
customer4.name = "Noah"
customer4.email = "Noah004@gmail.com"
customer4.address = "Kakiri"

customer5 = Customer()
customer5.customer_id = "customer005"
customer5.name = "Shavin"
customer5.email = "shavin005@gmail.com"
customer5.address = "Kireka"
print(f"{customer5.name} with id number {customer5.customer_id} lives in {customer5.address}.")

#no.3
class Restaurant:

    name = "2K ireka"
    address = "Ntinda"
    cuisine = "Greek food"
    rating = "five stars"

restaurant2 = Restaurant()
restaurant2.name = "Enro hotel"
restaurant2.address = "Mityana"
restaurant2.cuisine = "Local food"
restaurant2.rating = "Three stars"

restaurant3 = Restaurant()
restaurant3.name = "Eden hotel"
restaurant3.address = "Nsambya"
restaurant3.cuisine = "Japanese food"
restaurant3.rating = "Three stars"

restaurant4 = Restaurant()
restaurant4.name = "Luwombo hotel"
restaurant4.address = "kireka"
restaurant4.cuisine = "Local food"
restaurant4.rating = "Four stars"

restaurant5 = Restaurant()
restaurant5.name = "London Bridge"
restaurant5.address = "FortPortal"
restaurant5.cuisine = "Chinese food"
restaurant5.rating = "Five stars"

print(f"{restaurant5.name} in {restaurant5.address} serves the best {restaurant5.cuisine}.")


#no.4

class Movie:
    title = "Fast & Furious"
    director = " Jack O'Reilly"
    genre = "Action Movie"

movie2 = Movie()
movie2.title = "Hard Target"
movie2.director = "Jack Bucket"
movie2.genre ="Action Movie"

movie3 = Movie()
movie3.title = "Die Hard"
movie3.director = "Jack Boehner"
movie3.genre ="Action Movie"

movie4 = Movie()
movie4.title = "Megan"
movie4.director = "Jenny Green"
movie4.genre ="Sci-Fi Movie"

movie5 = Movie()
movie5.title = "Twins"
movie5.director = "Jane Doe"
movie5.genre ="Horror Movie"
print(f"{movie5.title} was directed by {movie5.director} and it was a {movie5.genre}.")

#no.5
class Course:
    name = "Education"
    instructor = "MR.Kigundu Hassan"
    student = "Kimuli Godrefy"

course2 = Course()
course2.name = "Block chain"
course2.instructor = "MR.kakungulu Emmanuel"
course2.student = "Kigozi Farouq"

course3 = Course()
course3.name = "Criminal Law"
course3.instructor = "Mr.Mawejje Patrick"
course3.student = "Ssebunya Ibrahim"

course4 = Course()
course4.name = "Civil Engineering"
course4.instructor = "Mrs.Nabbongo Betty"
course4.student = "Nakimuli Claire"

course5 = Course()
course5.name = "Medicine"
course5.instructor = "MR.Kasozi Mike"
course5.student = "Kigozi Farouq"
print(f"{course5.name} is taught by {course5.instructor} to a student known as {course5.student}.")

#no.6
class School:
    name = "Mase Junior School"
    address = "Kiwatule"
    principal = "Sserunjogi John"

school2 = School()
school2.name = "London college"
school2.address = "Nansana"
school2.principal = "Katongole Leonard"

school3 = School()
school3.name = "Riverdale Preparatory School"
school3.address = "Kyebando"
school3.principal = "Faith Komugisha"

school4 = School()
school4.name = "Cambridge International School"
school4.address = "Munyonyo"
school4.principal = "Cornerstone Divinci"

school5 = School()
school5.name = "Kings way High School"
school5.address = "Entebbe"
school5.principal = "Ssentongo Lordes"
print(f"{school5.name} is located in {school5.address} and headed by {school5.principal}.")

#no.7
class Rectangular_box:
    width = "3cm"
    height = "4cm"
    color = "red"

rectanglebox2 = Rectangular_box()
rectanglebox2.width = "5cm"
rectanglebox2.height = "4cm"
rectanglebox2.color = "green"

rectanglebox3 = Rectangular_box()
rectanglebox3.width = "6cm"
rectanglebox3.height = "5cm"
rectanglebox3.color = "purle"

rectanglebox4 = Rectangular_box()
rectanglebox4.width = "7cm"
rectanglebox4.height = "12cm"
rectanglebox4.color = "blue"

rectanglebox5 = Rectangular_box()
rectanglebox5.width = "7cm"
rectanglebox5.height = "14cm"
rectanglebox5.color = "orange"
print(f"I have an {rectanglebox5.color} rectangular box with width {rectanglebox5.width} and height {rectanglebox5.height}.")

#no.8
class Product:
    name = "books"
    price = "shs.450000"
    description = "Not fragile"

product2 = Product()
product2.name = "television"
product2.price = "shs.1,500,000"
product2.description = "Fragile"

product3 = Product()
product3.name = "television"
product3.price = "shs.1,500,000"
product3.description = "Fragile"

product4 = Product()
product4.name = "hand bag"
product4.price = "shs.15000"
product4.description = "Not Fragile"

product5 = Product()
product5.name = "Cups"
product5.price = "shs.50000"
product5.description = "fragile"

print(f"{product5.name} are sold at {product5.price} because they are {product5.description}.")

#no.9
class Bank:
    name = "Centenary Bank"
    branch = "Mityana branch"
    location = "Mityana"

bank2 = Bank()
bank2.name = "DFCU bank"
bank2.branch = "Kampala branch"
bank2.location = "Wandegeya"

bank3 = Bank()
bank3.name = "Stanbic bank"
bank3.branch = "Kampala branch"
bank3.location = "Katikamu"

bank4 = Bank()
bank4.name = "Absa bank"
bank4.branch = "Kampala branch"
bank4.location = "Wakiso"

bank5 = Bank()
bank5.name = "Cairo bank"
bank5.branch = "Kampala branch"
bank5.location = "Kiwatule"
print(f"{ bank5.name } , { bank5.branch } located at { bank5.location} provides good services.")


#no.10
class Song:
    title = "say it!"
    artist = "Chris Brown"
    duration = "3 minutes"
    
song2 = Song()
song2.title = "My heart"
song2.artist = "Serena Gomez"
song2.duration ="3 minutes"

song3 = Song()
song3.title = "Sitya danger"
song3.artist = "Alien skin"
song3.duration ="3.5 minutes"

song4 = Song()
song4.title = "Favourite song"
song4.artist = "Toosi"
song4.duration ="2.9 minutes"

song5 = Song()
song5.title = "So low"
song5.artist = "Remmy boys"
song5.duration ="4 minutes"
print(f"{song5.artist} sang a song called {song5.title} and it runs for {song5.duration}.")