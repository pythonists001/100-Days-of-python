print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
'''
small pizza: $15
Medium pizza: $20
Large Pizza: $25

pepperoni for small pizza: +$2
Pepperoni for Medium or Large Pizza: +$3

Extra cheese for any size pizza: +$1
'''
if size.upper() == "S":
  bill += 15
elif size.upper() == "M":
  bill += 20
else:
  bill += 25

'''
if add_pepperoni.upper() == "Y" and size.upper() == "S":
  bill += 2
elif add_pepperoni.upper() == "Y" and ( size.upper() == "M" or size.upper() == "L" ) :
  bill += 3
'''

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese.upper() == "Y":
  bill += 1

print(f"Total bill for your pizza is ${bill}.")
