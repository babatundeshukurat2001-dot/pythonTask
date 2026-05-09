
1.# ask user for x and y
2. #if x > 0 and y > 0 then
      # print "Q1"
  # elif x < 0 and y > 0 then
       #print "Q2"
   #elif x < 0 and y < 0 then
      # print "Q3"
   #elif if x > 0 and y < 0 then
      # print "Q4"
   #elif y == 0 and x != 0 then
      # print "x-axis"
   #elif x == 0 and y != 0 then
      # print "y-axis"
   ##else:
      # print "Origin"

x = int(input("Enter x: "))
y = int(input("Enter y: "))

if x > 0 and y > 0:
    print("Q1")
elif x < 0 and y > 0:
    print("Q2")
elif x < 0 and y < 0:
    print("Q3")
elif x > 0 and y < 0:
    print("Q4")
elif y == 0 and x != 0:
    print("x-axis")
elif x == 0 and y != 0:
    print("y-axis")
else :
    print("Origin")


