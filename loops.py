#A loop is an instruction that tells a computer to repeat the performance of a certain task.
#for loop (for) 
#Loops are when an entire block of
#code continues to run over and over again until the condition set is no longer valid.
# it iterates around all items.

def my_count():
    for item in range(10):# key words for,in,range...item can be any word of your choice.(item is a variable of your choice)
        print(item)

my_count()
# accessing a list element usimg a  for loop.
def examp2():
    langs = ["python","javascript","c++","ruby","nodejs"]
    for lang in langs:
        print(lang)

examp2()

def examp3(num):
    for number in range(num):
        print(number)

examp3(5)

def my_lang():
    langs = ["python","javascript","c++","ruby","nodejs"]
    for lang in langs:
        if lang == "python": # condition
            print("Your currently in python class")

my_lang()

def even(num):
    for number in range(num):
        if number % 2 == 0:
            print(number)

even(10)
            
# Alter that function to odd and it should give us odd numbers.

def odd(num):
    for number in range(num):
        if number % 2 != 0:
            print(number)

odd(10)

def pwr(p):
    my_po = p**2 
    if my_po % 2==0:
        print("The power is even")
    else:
        print("The power is an odd number")

pwr(11)



