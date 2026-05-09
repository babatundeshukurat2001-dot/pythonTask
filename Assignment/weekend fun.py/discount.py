#1. ask user for total_bill
#2. ask user if they are a member, store as is_member
#3. if total_bill >= 1000 andis_member == "yes" then
      # Set discount = 10%
      # Set message = "10% discount applied"
   #elif total_bill >= 1000 then
       #Set discount = 5%
      # Set message = "5% discount applied"
   #elif
       #Set discount = 0%
      # Set message = "No discount"
#4. Calculate final_amount = total_bill - (total_bill * discount)
#5. print message
#6. print final_amount.


total_bill = float(input("Enter total bill: "))
is_member = input("Are you a member? (yes/no): ").lower()

if total_bill >= 1000 and is_member == "yes":
    discount = 0.10
    message = "10% discount applied"
elif total_bill >= 1000:
    discount = 0.05
    message = "5% discount applied"
else:
    discount = 0
    message = "No discount"

final_amount = total_bill - (total_bill * discount)
print(message)
print("Final amount:", final_amount)
