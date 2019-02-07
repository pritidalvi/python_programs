import random

def search(list_in,user_in):
	for i in list_in:
		if i ==user_in:
			return True
		else:
			return False
if __name__=="__main__":
	list_in=set(random.sample(range(1,100),12))
	user_in=int(input("enter a number to check its existence in randomly generated list : "))
	answer=search(list_in,user_in)
	print(answer)


