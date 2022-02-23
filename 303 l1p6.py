#Given a positive integer n (read from the user), 
#write a Python program to find the n-th Fibonacci number based on the following assumptions.
#Fn = Fn-1 + Fn-2 where F0 = 0 and F1 = 1

f1 = 0
f2 = 1
fn = 0
n = int(input("Enter a number : "))
if n == 0:
    print("0")
elif n == 1:
    print("1")
else:
    for x in range(2,n+1):
        fn = f1+f2
        f1 = f2
        f2 = fn
    print(fn)
    