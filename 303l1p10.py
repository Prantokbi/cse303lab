#Given a list of numbers (hardcoded in the program), 
#write a Python program to find the second largest element of the list.

def secondlargest_number_2019_3_60_021(l):
    """Returns second largest number"""
    i= 0
    for x in l:
        if i<x:
            i=x
    k=0
    for y in l:
        if k<y and y!=i:
            k=y
    return k

l=[10,15,20,5,3,2]
print(secondlargest_number_2019_3_60_021(l))