#Given a string, find the count of the substring “CSE303” appeared in the given string. 
#Do not use any built-in function.

string = input()
n=6
i=0
c=0
while i<len(string):
    if(string[i:n] == 'CSE303'):
        c=c+1
        i=i+1
        n=n+1     
    else:   
        i=i+1
        n=n+1    
print(c)
    