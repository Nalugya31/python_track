def main():
    #List, tuples and dictionary in details.
    #acessing one value in a list
    # And the indices[labels] range from zero(0)
    # to move back wards we use -negatives.(but we dont hv negative 0 so begin from -1)
    # A list is a mutable data type.
    # its a variable that stores more than one value.
    my_nums = [0,1,2,3,4,5,6,7,8,9]
    my_nums2 = [10,20,30,40,50]
    osman = [100,[200]]
    osman2 = [1000,[[2000,3000]]]
    print(my_nums[5])
    print(my_nums2[4])
    print(my_nums2[-1])
    print(osman[0])
    print(osman[-2])
    print(osman[1][0])
    print(osman2[1][0][1])

main()

''''
Single line comments can be put in the function
Multline comments are supposed to be on top of the functions.
'''

def mutable():
    # Example of mutable list(open list)
    # you can add a value to a list using .append
    #.pop() means delete the value(begining with the last item)
    # .remove removes a specific item from a list
    osman.append(1000)
    osman.pop()
    print(osman)
    fruit = ["orange","pineapple"]
    fruit.append("apple")
    fruit.pop()
    print(fruit)
    fruit.remove("orange")
    print(fruit)

mutable()


    










def  tuples():
    #my tuples
    #Immutable list
    # Here we can only access values but we can't add or remove anything
    # we access values the same way as a list.
    my_tuple = (10,30,20,40,50)

tuple()



def dict():
    #Dictionary{dict} - mapping
    #its identified by braces{}
    # its mutable(add and remove anything)
    #to see indices or keys we use .keys()
    # to see the values we use .values()
    # if you want to remove use .delete("value")
    zebra = {"name":"hamlet", "legs":4, "color":"black&white", "sex" : "male"}
    print(zebra.keys())
    print(zebra.values())
    zebra.__delitem__("name")
    print(zebra)
dict()

 
'''
Exercise for definitions.
Defining functions in my list
'''
def numbers():
    my_nums = [0,1,2,3,4,5,6,7,8,9]
    print(my_nums[3])

numbers()



def numbers2():
    #Defining functions in my list

    my_nums2 = [10,20,30,40,50]
    print(my_nums2[3])

numbers2()

#My osman function stsrts here
def osman():
    
    my_list1 = [100,[200]]
    print(my_list1[0])

osman()

def osman2():
    #Defining my function as osman.
    my_list3 =[1000,[[2000,3000]]]
    print(my_list3[1][0][1])

osman2()

# My fruit function starts here
def fruits():
   
    sugarly = ["orange","pineapple","apple"]
    print(sugarly[1])
    
fruits()

    #my trial function starts here
def trial():
   my_tuple = (10,30,20,40,50)
   print(my_tuple[2])

trial()



