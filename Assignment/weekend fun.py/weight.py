
#1. ask user for weight in kg
#2. ask user for height in meters
#3. calculate bmi = weight / (height * height)
#4. iF bmi < 18.5 THEN
      # print "Underweight"
 #  elif bmi < 25 THEN
     #  print "Normal"
   # elif bmi < 30 THEN
      # print"Overweight"
  # else
       #print "Obese"


weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height * height)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
