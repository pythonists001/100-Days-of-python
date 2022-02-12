print("Welcome to the tip calculator.")
bill_amount = float(input("What was the total bill? $"))
tip = int(input("What precentage tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))
## bill per person
total_bill = bill_amount * (1 + (tip / 100))
bill_per_person = round(total_bill / num_people, 2)
bill_per_person = "{:.2f}".format(bill_per_person)  ## to print values to two places after decimal
print(f"Each person should pay : ${bill_per_person}")
