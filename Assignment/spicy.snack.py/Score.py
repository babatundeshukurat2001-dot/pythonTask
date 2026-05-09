score1 = int(input("Enter first number: "));
score2 = int(input("Enter second number: "));
score3 = int(input("Enter third number: "));
 
average = score1 + score2 + score3 / 3;

if (average >= 90):
    print("A")

elif(average >= 80): 
    print("B")

elif(average >= 70):
    print("C")

elif(average >= 60):
    print("D")

else:
    print("F")
