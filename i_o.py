#In python two we had raw input(strings) and input(integer) while in python 3 we only have input to capture values from the key board.
# however in python 3 input accepts everything as a string.
# In python 2 print was just a statement where by we could write print "" but in python 3 its a function
# Input captures everything as a string. 
# we cant pass an argument as a string.
# type casting is converting a value from one data type to another.
def payee(name,salary):
    rate = 0.3
    tax = rate*salary
    net = salary-tax
    print("*************")
    print("Dear:", name)
    print("Your payable tax is: ",tax )
    print("And your total salary is: ", net)
    print(".....................")





print("Your welcome! Please follow the instructions ") 
name = raw_input("Please enter your name: ")
salary = input("please enter your salary: ")

payee(name,salary)         



def mine(school,name,email):
    print(school,"Is expensive")
    print("your female",name)
    print("i like your address",email)


print("Your welcome to my page !")
school = raw_input("Enter your school name here: ")
name = raw_input("Enter your name: ")
email = raw_input("Enter your email address: ")
mine(school, name, email)



