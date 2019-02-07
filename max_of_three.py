#Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!

def max(a,b,c):
	if a > b:
		if a > c:
			return a
		else:
			return c
	elif b > c:
			return b
	else:
			return c



if __name__=="__main__":
	input1=int(input("Enter first number to find max number between three numbers : "))
	input2=int(input("Enter second number to find max number between three numbers : "))
	input3=int(input("Enter third number to find max number between three numbers : "))
	max_num=max(input1,input2,input3)
	print("Max number among above number is : %d"%max_num)
