1. #Ask user for integer x
2. #Ask user for integer y
3. #IF y equals 0 THEN
       #PRINT "cannot divide by zero"
   
#ELSE
      # PRINT x divided by y



x = int(input("Enter first integer: "))
y = int(input("Enter second integer: "))

if y == 0:
    print("cannot divide by zero")
else:
    print(x / y)




