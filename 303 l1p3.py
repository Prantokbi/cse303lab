#Write a Python program to calculate the compound interest based on the given formula. 
#Read inputs from the user.
#A = P * (1 + R/100)
#T where P is the principle amount, R is the interest rate and T is time (in years).
#Define a function named as compound_interest_<your-student-id> in your program.

def compound_interest_2019_3_60_021(P,R,T):
    """Calculates compound interest"""
    A = P * (1 + R/100)**T
    return A

print(compound_interest_2019_3_60_021(10, .2, 2))