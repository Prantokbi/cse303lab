#Given a list of numbers (hardcoded in the program), 
#write a Python program to calculate the sum of the even-indexed elements in the list.

l = [10,20,30,40]
s = 0
i = 0
while i<len(l):
    s=s+l[i]
    i=i+2
print(s)