#age(year of birth),location and type of work

def payee(name,salary,age,location,work):
    
    # here we are trying to find the tax paid and the remaining net pay.
    rate = 0.3
    if salary>=300000:
      tax = rate*salary
      net = salary-tax
      print("*************")
      print("Dear:", name)
      print("You'are: ", age,"years")
      print("Your district is: ", location)
      print("Your work type is: ", work)
      print("Your payable tax is: ",tax )
      print("And your total salary is: ", net)
      print(".....................")
    else:
       print("Dear:", name)
       print("Your salary is non-taxable")




print("Your welcome! Please follow the instructions ") #This will come on top of the page.
name = raw_input("Please enter your name: ")# prompt the user to enter their name.
year_of_birth = input("Please enter your year of birth: ")# prompt the user to enter their year of birth.
age = 2023-year_of_birth # This will help us determine the age of the user.
location = raw_input("Please enter location: ") # This will help us determine the location of the user.
work = raw_input("Please enter your work type here: ") # This will help us determine the work type of the user.
salary = input("please enter your salary: ")# prompt the user to enter their salary.

payee(name,salary,age,location,work)   


def exmp():
   my_numbers = []
   num = input("Enter your lucky number:")
   my_numbers.append(num)
   for i in my_numbers:# you only print out items in the list not the whole list.
      print(i)
exmp()
