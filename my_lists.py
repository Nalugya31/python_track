



prime_numbers = [2,5,7,9,11] 
friends = ['van','ttrinity','julie','charlie']
print(friends[2])
print(prime_numbers[3])
football = ['uganda','kenya','tanzania',['paris','tottenum']]
print(football[0])
print(football[1])
print(football[2])
print(football[3])
print(football[3][0])
print(football[3][1])
football2 = ['uganda','kenya','tanzania','rwanda',['paris','tottenum','burundi']]
print(football2[4][0])
print(football2[4][2])
osman2 = [1000,[[2000,3000],['van','julie']],'end of list']
print(osman2[-1])
print(osman2[2])
print(osman2[-3])
print(osman2[1][0][1])
print(osman2[1][1][0])
print(osman2[1][0][0])
print(osman2[1][1][1])
osman = [1000,2500,[[2000,3000],['van','julie']],'end of list']
print(osman[2][0][0])
osman.remove(1000)
print(osman)
friends2 = ['van','ttrinity','julie','charlie']
friends2[3]="monica"
print(friends2)
numbers = [99,33,55,66,22,40]
numbers.insert(2,46)
print(numbers)

#x = input("What is x?")
#if x%2 == 0:
    #print("Even")
#else:
   # print("Odd")
# returning a number
def cube(number):
   return number*number*number

number = int(input("Enter the number:"))
print(cube(number))

'''
This code below determines the higher test score between test1 and test2 and returns that value.
'''


def tests(test1, test2):
	#test1 and test2 are parameters.
	if test1 == test2:
		#If the value of test1 is equal to the value of test2 return the value of test1.
		return test1
	else:
		# But if the value of test1 is not equal to the value of test2 return the value of test2.
		return test2
#Prompt the user to enter marks here
test1 = int(input('Please enter Marks for test one: '))
test2 = int(input('Please enter Marks for test two: '))

'''
In the code below, 
it helps to calculate  the final crswork marks based on the provided crswork marks and the marks obtained in two tests. 
It then prints the final crswork marks for the user.

'''
def courseWrk(cswork):
	#cswork is a parameter of courseWrk function.
	testsMark = tests(test1,test2)
	# Call the tests function with its paramenters and assign the result to testsMark
	avgtestsCswork = (cswork + testsMark)/2
	# Calculate the average of cswork and testsMark
	fnltestsCswork = avgtestsCswork * (40/100)
	#Calculate the final cswork marks as 40% of the average
	print('..............................')
	#Print the final cswork marks
	print('your final coursework marks is: ', fnltestsCswork)
	print('..............................')
# Allow the user to enter cswork marks here
cswork = int(input('Please enter your course work Marks: '))
#Call the courseWrk function with cswork as its parameter.
courseWrk(cswork)


   






        



