from pybank import *
message = """1. Register
2. Login
3. Calculate Balance
4. Apply Interest
5. Summary
6. Exit : """

# You'll need these functions defined above
def validate_email(email):
    return "@" in email and "." in email

def is_strong_password(password):
    return len(password) >= 8

# Store user data
user_data = {"email": None, "password": None, "balance": 0.0}
interest_rate = 0.05  # 5% annual

while True:
    user_input = input(message)
    match user_input:
        case "1":
            email = input("Enter email: ")
            password = input("Enter password: ")
            if validate_email(email) and is_strong_password(password):
                user_data["email"] = email
                user_data["password"] = password
                print("Registration successful")
            else:
                print("Registration failed. Check email format and password length >= 8")

        case "2":
            email = input("Enter email: ")
            password = input("Enter password: ")
            if user_data["email"] == email and user_data["password"] == password:
                print("Login successful")
            else:
                print("Login failed")

        case "3":
            transactions = []
            amount = float(input("Enter amount or 0 to stop: "))
            while amount != 0:
                transactions.append(amount)
                amount = float(input("Enter amount or 0 to stop: "))
            user_data["balance"] = sum(transactions)
            print(f"Current balance: {user_data['balance']}")

        case "4":
            if user_data["balance"] > 0:
                interest = user_data["balance"] * interest_rate
                user_data["balance"] += interest
                print(f"Interest of {interest:.2f} applied. New balance: {user_data['balance']:.2f}")
            else:
                print("Balance is 0 or negative. No interest applied.")

        case "5":
            print("\n--- Account Summary ---")
            print(f"Email: {user_data['email']}")
            print(f"Balance: {user_data['balance']:.2f}")
            print(f"Interest Rate: {interest_rate * 100}%")
            print("----------------------\n")

        case "6":
            print("Exiting. Goodbye!")
            break

        case _:
            print("Invalid option. Choose 1-6.")
                
          
