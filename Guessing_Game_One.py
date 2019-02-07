#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
import random
number=random.randint(1,9)

i=1
cont='yes'
while cont!='exit':
	a=int(input("guess any random number between 1 to 9 : "))
	if a > number:
		print("too high")
	elif a < number:
		print("too low")
	else:
		print("you have guessed correct number")
		i=+1
		print("you have guessed correct number %s times"%i)
	cont=input("do you wish to continue?if yes, please type yes else type exit ").lower()
	
	