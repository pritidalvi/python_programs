#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

number=int(input("Enter a number "))
ans=[]
for i in range(1,number):
	if number%i==0:
		print("enter number is divisible by "+str(i))
		ans.append(i)
print ("List of divisor for entered number is " +str(ans))
