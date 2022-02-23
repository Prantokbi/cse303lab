#Given a string, display only those characters which are present at an even index number. 
#Read inputs from the user.

string = input()
i=0
while i<len(string):
    print(string[i])
    i=i+2
    