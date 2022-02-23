#Given a positive integer N (read from the user)
#write a Python program to calculate the value of the following series.
#1^2 + 2^2 + 3^2 + 4^2 ..... + N^2

n=int(input("Enter range "))
s=0
for x in range(1,n+1):
    s =s+x**2
print(s)
    