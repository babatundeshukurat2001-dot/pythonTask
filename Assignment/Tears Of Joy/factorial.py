n = int(input("Enter a number: "))
if n < 0:
    print ("factorial not defined for negetive numbers")
else:
    factorial = 1
    i = 1
while i <= n:
    factorial = factorial * i
    i = i + 1 
print(f"The factorial of {n} is {factorial}")
