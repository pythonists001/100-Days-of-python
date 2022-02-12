print("Welcome to Leap year calculator")
year = int(input("Enter the year to check if it's Leap year or not ? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not Leap Year")
    else:
        print("Leap Year")
else:
    print("Not a Leap Year.")
