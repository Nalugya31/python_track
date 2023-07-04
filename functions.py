#we can group code relatable to each other and give it a name.
# group of statements relatable to each other is a function.
#mod() calling a function above or envoking the function
#num = 50
#num1 = 100
#num3 = num + num1
#print(num3)

def sum():
    num,num1 = 20,30
    num3=num + num1
    print(num3)

sum()

def sub():
    num,num2 = 50,10
    num3 = num - num2
    print(num3)

sub()

def mod():
    num,num2 = 25,2
    num3 = num%num2
    print(num3)

mod()

# a list that has numbers from 1 to 10.
def my_list():
    list1 = [1,2,3,4,5,6,7,8,9,10]
    print(list1[0])

my_list()


# user defined functions eg payee
# pre-defined functions e.g print,input(values from the keyboard)

