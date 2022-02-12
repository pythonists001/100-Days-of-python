print("Leap year calculator")
leap_year = False
year_to_check = int(input("Enter the year to check if it's leap year or not? "))
if year_to_check % 4 == 0 and (year_to_check % 100 != 0 or year_to_check % 400 == 0):
    leap_year = True

if leap_year:
    print(f"Year {year_to_check} is leap year.")
else:
    print(f"Year {year_to_check} is not a leap year.")
