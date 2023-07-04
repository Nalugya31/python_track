#age(year of birth),location and type of work
def payee(name,salary,age,location,work):
    rate = 0.3
    if salary>=300000:
      tax = rate*salary
      net = salary-tax
      print("*************")
      print("Dear:", name)
      print("Your payable tax is: ",tax )
      print("And your total salary is: ", net)
      print(".....................")
    else:
       print("Dear:", name)
       print("Your salary is non-taxable")




print("Your welcome! Please follow the instructions ") 
name = raw_input("Please enter your name: ")
age = input("Please enter your age: ")
location = raw_input("Please enter location: ")
work = raw_input("Please enter your work type here: ")
salary = input("please enter your salary: ")

payee(name,salary,age,location,work)   