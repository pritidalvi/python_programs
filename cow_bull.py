import random
cows=0
bulls=0
count=0
number=str(random.sample(range(1,9),4))
guess=list(input("Enter 4 digit number to guess : "))
number=[6,6,6,6]
print (list((map(int,guess))))
print(number)
if number==list((map(int,guess))):
	count=+1
	print("congratulation!!you have guess number correctly")
	print("you have make %d guesses till now"%count)
	sys.exit()
while number != list(map(int,guess)):
	for i in number:
		if i in guess:
			cows=+1
		else:
			bulls=+1
	count=+1		
	print("you have %d cows and %d bulls"%(cows,bulls))	
	guess=list(input("Enter 4 digit number to guess : "))
print("you have make %d guesses till now"%count)
		
