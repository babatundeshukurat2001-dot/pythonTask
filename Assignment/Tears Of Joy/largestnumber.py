"""
using while loop to print factorial number. collect input, when largest is equal to 0. then collect input again and print the largest



"""

count = input("Enter: ")
largest = None

while count!= "done" :
    num = int(count)
    if largest is None or num > largest:
        largest = num
    count = input("Enter: ")
print("largest: ", largest)
