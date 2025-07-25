#ASSIGNMENT 3:
n1 = int(input('Enter a number: '))

#Module 4: Functions & Modules in Python
#Task 1: Calculate Factorial Using a Function
def factorial(n1):
    if n1 < 2:
        return 1
    else:
        return n1 * (factorial(n1-1))


resultFact = factorial(n1)
print(f'Factorial of {n1} is: {resultFact}')


#Task 2: Using the Math Module for Calculations
import math

n2 = int(input('Enter a number: '))

def sqrt(n):
    return n ** 0.5

resultSqrt = sqrt(n2)

print(f'Square root: {resultSqrt}')

def natural_log(n):
    if n<=0:
        print('Input must be a positive number.')
    return math.log(n)

resultLog = natural_log(n2)

print(f'Logarithm: {resultLog}')

def sine_radian(n):
    return math.sin(n)

resultSine= sine_radian(n2)
print(f'Sine: {resultSine}')






