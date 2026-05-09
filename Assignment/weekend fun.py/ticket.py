#1. ask user for age
#2. iF age is less than 5 then
# print "free"
   #else age is 5 to 12 then
      # print "$5"
  # elif age is 13 to 64 then
       #print "$12"
  # else
      # print "$8"


age = int(input("Enter age: "))

if age < 5:
    print("free")
elif age <= 12:
    print("$5")
elif age <= 64:
    print("$12")
else:
    print("$8")
