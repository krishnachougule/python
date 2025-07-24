#Assignment 2
#Module 3: Control Structure in Python

#Task1: Check if a Number is Even or Odd

number = int(input('Enter a number: '))
rem = number%2
if rem == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")



#Task2: Sum of Integers from 1 to 50 using loop
total=0
for i in range(1,51):
    total +=i

print(f'the sum of the numbers from 1 to 50 is {total}')

