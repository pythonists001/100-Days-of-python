print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print(f"Please pay ${bill}")
    elif age <= 18:  ## since age case for <12 already there, this will check if age is less then equal to 18 iff 1st if not satisfied
        ## which implies age lies between 12 to 18
        bill = 7
        print(f"Please pay ${bill}.")
    elif age >= 45 and age <= 55:  ## mid-life crisis bracket
        print("Everything is going to be ok. Have a free ride on us !")
    else:
        bill = 12
        print(f"Please pay ${bill}.")

    wants_photo = input("Do you want a photo taken? Y or N ")
    if wants_photo.upper() == "Y":
        bill += 3

    print(f"Your final bill is ${bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")
