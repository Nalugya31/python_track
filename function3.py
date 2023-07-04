# These functions are called static parameters.
def add(num1,num2):
    num3 = num1 + num2
    print(num3)


def sub(num1,num2):
    num3 = num1 - num2
    print(num3)

#Allowing functions to communicate
def add2(num1,num2): #num1 and num2 are parameters

    num3 = num1 + num2
    return num3

def sub2(num1):
    num3 = add2(5,3) - num1
    print(num3)
sub2(3) # 3 here is an argument or actual/ formal parameter.
'''
 >The above functions are called dynamic functions or parameterised functions.
 >Dynamic fuctions are  functions that can be modified,created and called at the runtime.
 >Static dunctions are functions that belong to a certain class and are independent of any specific object of that class. or those functions that dont hv paramenters.
>Return stops the whole process of the code
>When you print a function call wihout a return statement you will get a value called "None".
>A function that calls a value of a return statement from another function is called a calling function.
'''

