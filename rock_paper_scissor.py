Player1=input("enter your name player 1 : ")
Player2=input("enter your name player 2 : ")
a=input("%s,choose either rock/paper/scissor : "%Player1).lower()
b=input("%s,choose either rock/paper/scissor : "%Player2).lower()
play_cards = ['rock','paper','scissor']
if a  not in play_cards:
   a=input("%s,choose either rock/paper/scissor : "%Player1).lower()
elif b  not in play_cards:
   b=input("%s,choose either rock/paper/scissor : "%Player2).lower()
else:
   print("Lets Play")

if a==b:
	print("Its a tie between you two",)
elif a=="rock":
	if b=="scissor":
		print("Player %s i.e. rock wins"%Player1)
	else:
		print("Player %s i.e. paper wins"%Player2)
elif a=="scissor":
	if b=="paper":
		print("Player %s i.e. scissor wins"%Player1)
	else:
		print("Player %s i.e. rock wins"%Player2)
elif a=="paper":
	if b=="rock":
		print("Player %s i.e. paper wins"%Player1)
	else:
		print("Player %s i.e. scissor wins"%Player2)
else:
	print("wrong input!!Please enter rock or paper or scissor to continue")













