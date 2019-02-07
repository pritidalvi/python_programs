occurence={}
count=0
with open('my_first_file.txt','r') as open_file:
	for i in open_file.readlines():
		print(i)
		if i.rstrip('\n') in occurence:
			occurence[i.rstrip('\n')]+=1
		else:
			count=1
			occurence[i.rstrip('\n')]=1
print(occurence)



	 
