n= int(input("enter a nonnegative integer:"))
if n < 0:
  print("factorial is not defined for negative numbers.")

 else:

  factorial = 1
for i in range(1, n + 1):
   factorial *= i
print(f"(n)! = (factorial)")
