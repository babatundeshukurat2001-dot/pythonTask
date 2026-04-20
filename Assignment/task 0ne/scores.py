number = input("enter your number")
number = int(number)

if(number >= 90):
  print("you scored A")

elif(number >= 80 or number >= 89):
  print("you scored B")

elif(number >= 70 or number >= 79):
  print("you scored C")

elif(number >= 60 or number >= 69):
  print("you scored D")

else:
  print("you scored F") 
