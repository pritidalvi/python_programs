#Ask the user for a string and print out whether this string is a palindrome or not.

a_string=input("Enter a string to find if it is palindrome or not : ")
reverse_string=a_string[::-1]
if a_string==reverse_string:
	print("Entered string is palindrome")
else:
	print("Entered string is not palindrome")
