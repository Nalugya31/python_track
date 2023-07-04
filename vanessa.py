
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