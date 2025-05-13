#TASK 1

n=int(input('Enter a number:'))
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * (factorial(n-1))
result = factorial(n)
print('Factorial of',n,'is:',result)

#TASK 2
n=int(input('Enter a number:'))
def op1():
    import math
    print('square root:',math.sqrt(n))
    print('Logarithm:',math.log(n))
    print('Sine',math.sin(n))
op1()