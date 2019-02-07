#Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.

def fibo(number):
	fib=[]
	count=0
	while count <= number:
		if count==0:
			a=1
			b=1
			fib.append(a)
			fib.append(b)
			count+=1
		else:
			c=a+b
			fib.append(c)
			a=b
			b=c
			count+=1
	print("your fibonacci series is here : "+str(fib))

number=int(input("how many fibonacci series to generate : "))
fibo(number)

	