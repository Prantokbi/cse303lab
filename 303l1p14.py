#Given a string, write a python program to check if it is palindrome or not. 
#Define a function named palindrome_checker_<your-student-id> in your program.
def palindrome_checker_2019_3_60_021(string):
    """Checks if a string is palindrome or not.""" 
    n=len(string)
    i=0
    while i<n//2:
        if string[i] !=  string[n-1-i]:
            return False
        i=i+1
    return True


s= input("Enter a string: ")
if palindrome_checker_2019_3_60_021(s):
    print("Palindrome")
else:
    print("Not palindrome")