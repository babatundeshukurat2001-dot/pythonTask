password = input("Enter your password: ")
length = len(password)

if length < 1:
    print("Invalid: Password cannot be empty")
elif length < 6:
    print("Weak")
elif 6 <= length <= 10:
    print("Medium")
else:  
    print("Strong")
