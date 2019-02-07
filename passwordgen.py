#Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password.
import string
import random

def passwordgen() :
	lower_letter=string.ascii_lowercase
	upper_letter=string.ascii_uppercase
	digits=string.digits
	punct=string.punctuation
	final_list=''.join((random.choices(string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation,k=8)))
	return (final_list)

password=passwordgen()
print("your newly generated password is"+str(''.join(password)))

