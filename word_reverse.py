#reverse word order

sent=input("Please enter eny one statement to reverse :")
statement=sent.split(" ")
print(statement)
reverse=' '.join(statement[::-1])
print(" your reverse statement is : "+str(reverse))


