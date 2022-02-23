#Given two integer numbers, write a Python program to return their product. 
#If the product is greater than 1000, then return their sum. Read inputs from the user.

a=int(input())
b=int(input())
if a*b>1000:
    print(a+b)
else:
    print(a*b)

