numbers = []

for i in range(3):
 num = int (input(f"enter integer(i+1): "))
 numbers.append(num)



total = sum(numbers)
average = total/3
product = 1
for num in numbers:
   product *= num

smallest = min(numbers)
largest = max(numbers)

print(f"\nsum")
print(f"average")
print(f"product")
print(f"smallest")
print(f"largest")
