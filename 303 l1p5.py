#Given a positive integer N (read from the user)
#write a Python program to check if the number is prime or not. 
#Define a function named as prime_find_<your-student-id> in your program.

def prime_find_2019_3_60_021(n):
    """Finds prime number"""    
    if n==1 or n==0:
        return False
    for x in range(2,n):
          if n%x==0:
            return False
    return True

n=int(input("Enter a number: "))
if prime_find_2019_3_60_021(n):
    print("prime")
else:
    print("not prime")     
    