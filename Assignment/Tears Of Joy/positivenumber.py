"""
using while loop,collect user_input,enter the number,then print user_input,and collect input again and enter number.Then print the positive number and user_input

"""
user_input =int(input("Enter number: "))


while user_input < 0:
    print(user_input)
    user_input = int(input("Enter number: "))

print("your positive number is: ", user_input)
