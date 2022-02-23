#Given a list of numbers (hardcoded in the program), 
#write a Python program to find the largest and smallest element of the list. 
#Define two functions largest_number_<your-student-id> and smallest_number_<your-student-id> in your program. 
#Do not use any built-in function.

def largest_number_2019_3_60_021(l):    
    """Returns largest number from a list"""
    i= 0
    for l in l:
        if i<l:
            i=l
    return i

def smallest_number_2019_3_60_021(l):
    """Returns smallest number from a list"""
    i= 99999
    for l in l:
        if i>l:
            i=l
    return i
    
l=[10,15,20,5,3,2]
print(largest_number_2019_3_60_021(l))
print(smallest_number_2019_3_60_021(l))
