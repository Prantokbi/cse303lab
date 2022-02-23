#Given a string and an integer number n. 
#Remove characters from a string starting from zero up to n and return a new string. 
#N must be less than the length of the string. Read inputs from the user. 
#Do not use any built-in function.

string = input()
n = int(input())
string=string[n:]
print(string)
    