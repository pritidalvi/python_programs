a_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print ("your list is");a_list
number=int(input("enter a number"))
ans=[]
len=len(a_list)
for i in a_list:
	if i <= int(number):
		print("element which is smaller is");i
		ans.append[i]
print ("newly created list having number smaller than number you entered is");ans


