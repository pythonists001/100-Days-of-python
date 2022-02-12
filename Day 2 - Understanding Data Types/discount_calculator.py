print("Welcome to the discount calculator.")
bill_amount = float(input("What was the total amount? ₹"))
discount_percent = float(input("What precentage discount would you like to give? 10, 20, or 50? "))
## bill per person
total_bill = bill_amount * (1 - (discount_percent / 100))
print(f"Total Amount to pay : ₹{total_bill}")
