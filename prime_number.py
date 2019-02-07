#Ask the user for a number and determine whether the number is prime or not.
def prime(number):
	count=0
	stop_number=number+1
	for i in  range(1,stop_number):
		if number%i==0:
			count+=1
	if count==2:
		print("entered number is prime")
	else:
		print("entered number is not prime")

number=int(input("Enter a number to check if it is prime or not : "))
prime(number)