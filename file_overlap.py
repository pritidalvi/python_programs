overlap=[]
with open ('prime_number.txt','r') as prime_number:
		b=prime_number.read()
with open ( 'happy_number.txt','r' ) as a:
	for i in a.readlines():
			if i.rstrip('\n') in b.rstrip('\n'):
				overlap.append(i.rstrip('\n'))
print(" overlapping number between two files are"+str(overlap))
			