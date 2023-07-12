'''
Is a piece of code that defines what an object to itself and  to others.
 And in methods we find there behaviour./ function statements.
 And  how do you do that particular thing.
 methods can be taken on from one object to another.
A function in sp is a method in oop.
the lines with in the function are called behaviours where as a function is a method 
All objects under the class should have the same methods.
it has attributes e.g. name, age
the things that it has are called methods or behaviours e.g def talk, def attend_class.
a function inside a class is a method or behaviour.
'''
 

class Girl:
    name = "Jessy" 
    age = 20
    gender = "female"
    size = "small"
    family = "kabaka"
    size_of_bra = "small"
    def dance():
        return "she likes maganda"
    
    def talk():# method
        print("This girl speaks politely")

    def greet():# method
        print("Hello, world!")# behavior
        return "" # to return a statement you have to have a print statement inorder not to hv none in the terminal.
Girl.greet()   
print(Girl.greet())# here some space will be left below the statement "Hello, world!"
Girl.talk() # here we have just called a method even if we dont have a return statement.
print(Girl.dance())# this prints out the behaviour of the method. and we use this when we have printed in the method.



#coaching
class Student:
    name = "Kapere" # attribute 
    age = 20
    address = "kakiri"
    phone_number = 702104389

    def assignment(): # method/behavior
        num = 2+3
       # return "complete assignment"
        #return num
        return [num, "complete assignment"]# this is used to return more than one thing and its a list.
    
print(Student.name,Student.age,Student.phone_number)
print(Student.assignment())



items = ["Uganda","Kenya","Tanzania","Rwanda"] # now info list is stored in the list.
for item in items:# for accessing items in the list.
    print(item)

print("--------------------------------")

for i in range(4,10): #its used to get a sequence of number with in the range.
    print(i)


print("--------------------------------")
# it runs until the condition is met or false.
cars = 1
while cars <= 10:
    print(cars)
    cars = cars + 2 
      
# else is always the last condition
gpa = int(input("Please enter the number:")) # here we are converting info.
if gpa < 0:
    print("Try fishing")
elif gpa == 1:
    print("You have tried")
elif gpa == 2:
    print("You have tried alittle more")
else:
    print("Good job!")


# a dynamic class.

    
