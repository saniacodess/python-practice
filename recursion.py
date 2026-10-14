# Recursion is a fumction that calls itself

# for finding the factorial of n

def factorial(n):
    if(n==1 or n==0):
     return 1
    return n * factorial(n-1)

n = int(input("Enter a number : "))
print(f" The Factorial of {n} is {factorial(n)}")
