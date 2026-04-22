"""
call out all the numbers given
using while loop,sum the total of each number given
divide it by the numbers  





"""


numbers = [4, 8, 15, 16, 23, 42, 10, 5, 4, 7, 20]
total = 0
count = 0
num = 0

while num < len(numbers):
    total += numbers[num]
    count += 1
    num += 1
average = total / count
print("numbers =", numbers , average)

