#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 

number=int(input("enter number to check if t odd or even"))
print ("number you enter is");number
if number%2==0:
	print ("You entered even number")
else:
	print ("you entered odd number")