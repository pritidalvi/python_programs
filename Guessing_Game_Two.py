#You, the user, will have in your head a number between 0 and 100. The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.
#At the end of this exchange, your program should print out how many guesses it took to get your number.
import random

count=0
flag='false'
user_input=random.randint(0,100)
print(flag)
print(user_input)
while flag=='false':
	for i in range(0,100):
		if i==user_input:
			print("Its a match")
			count+=1
			flag='true'
			break
		elif i < user_input:
			print("Too Low")
			count+=1
			i+=1
			flag='false'
			print(count)
		else:
			print("Too high")
			count+=1
			i+=1
			flag='false'
			print(count)

print("you have make %d guesses to guess correct"%count)
