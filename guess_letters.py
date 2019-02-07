print("welcome to the game of hangman")
input_word='evaporate'
input_word=list(input_word)
count=0
wrong_guess=[]
length=len(input_word)
correct_guess=list('*' *len(input_word))
letter=input("Guess the your letter :")
count=0
total_guess=6
while True:
	if letter in input_word:
		print("you are in if")
		print("input word :"+str(input_word))
		print("letter :"+str(letter))
		print("correct")
		index=input_word.index(letter)
		correct_guess[index]=letter	
		input_word[index]=''
		print("index"+str(index))
		print("input word :"+str(input_word))
		print("letter :"+str(letter))
	elif letter in wrong_guess:
		print("you are in elif")
		print("letter :"+str(letter))
		print("wrong_guess :"+str(wrong_guess))
		print("You have already guess this letter")
		letter=''
	else:
		print("you are in else")
		print("letter :"+str(letter))
		print(''.join(correct_guess))		
		if letter is not '':
			print("Incorrect guess!!")
			count+=1
			guess_left=total_guess-count
			print("You have only %d guess now"%guess_left)
			wrong_guess.append(letter)
		letter=input("Guess the your letter :")
	if '*' not in correct_guess:
		print("Congratulations!!You won this game")
		break
		



	