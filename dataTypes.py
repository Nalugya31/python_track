# Any character that is in ("") it is a string
#Categorization of values that are going to be stored in variable names to prevent computer memory wastage.
# Examples ;numeric data type,string,sequence,mapping,booleans,set,etc
# In numerics we have(int [whole number],float[decimal point],complex) e.g 
num1 = 1000
num2 = 1000.0
num3 = 1 + 2j
num4 ="1000" 

print(type(num1))
print(type(num2))
print(type(num3))
print(type(num4))

#String(str)
# any value in single or double quotes
name = "Vanessa"
print(type(name))
#Sequence ( list [a list can be for different data types],tuple,range)
my_list = [0,2,4,6]
print(type(my_list))
my_list2 = [0,2,4,6,"Vanessa",10.5]
print(type(my_list2))
#Tuple
my_tuple = (0,2,4,6)
print(type(my_tuple))
#Mapping(dict)
my_dict = {"uganda" : "kampala","Italy" :"Rome","France" :"Paris","Tanzania" : "Dodoma"}
print(type(my_dict))
#Booleans
name1 = True
name2 = False
print(type(name1))
#Set( a set gives you unordered list of items)
# It eliminates duplicated items.
my_set = {0,5,10,15,20}
my_set2 = {1,1,2,2,10,10,3,3}
print(my_set)
print(my_set2)
print(set(my_dict))
