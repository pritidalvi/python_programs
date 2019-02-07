#Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
import random
a=set(random.sample(range(1,30),2))
b=set(random.sample(range(1,30),3))
print("First set : "+str(a))
print("Second set : "+str(b))
print("List without duplicate :"+str(a|b))

## second approach
a=random.sample(range(1,30),2)
b=random.sample(range(1,30),3)
for i in a:
	if i not in b :
		b.append(i)
print("List without duplicate : "+str(b))


