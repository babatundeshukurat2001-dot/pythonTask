"""
using for loop,range number is equal to 1-51
so if the number is divided by 3 and is equal to 0,and also divided by 5 and is equal to 0,print fizzbuzz. but if the is just divide by 3 and gives 0,just print fizz. if the number is just divided by 5 and give 0,just print dizz.




"""

for number in range(1, 51):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Dizz")
