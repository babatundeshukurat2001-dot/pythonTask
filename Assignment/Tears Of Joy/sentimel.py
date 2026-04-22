total = 0
while  True:
    number = int(input("Enter an integer(0 to stop): "))
    if number == 0:
        break
    total += number
print ("total of all numbers: ", total)
