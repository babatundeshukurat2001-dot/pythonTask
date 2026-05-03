def validate_email(email):
    if "@" not in email:
        raise ValueError("Invalid Email")
    if email[0] == "@" or email[-1] == "@":
        return "Invalid email"
    if len(email) >= 8:
        return True
    return False
    
def calculate_balance(transactions):
    total = 0
    for amount in transactions:
        total += amount
    return total
        
def is_strong_password(password):
    return len(password) >= 8
    
def apply_interest(balance, rate, years):
    if rate < 0 or years < 1:
        raise ValueError("Invalid rate")
    compound_interest = balance * (1 + rate) ** years
    return round(compound_interest, 2)
    
def get_transaction_summary(transactions):
    total_credits = 0
    total_debits = 0
    net_balance = 0
    transaction_count = 0
    
    for transaction in transactions:
        if transaction[0] == "credit":
            total_credits += transaction[1]
        else:
            total_debits += transaction[1]
            
        transaction_count += 1
        
    net_balance = total_credits - total_debits
    
    return [["total_credits", total_credits], ["total_debits", total_debits], ["net_balance", net_balance], ["transaction_count", transaction_count]]





























