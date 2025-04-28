import math
def factorial_math(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    return math.factorial(n)

result=int(input("Enter number:"))
res=factorial_math(result)
print(res)


def factorial_math1(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n<=1:
        return 1
    else:
        return n*factorial_math1(n-1)
    
result=int(input("Enter number:"))
res=factorial_math1(result)
print(res)