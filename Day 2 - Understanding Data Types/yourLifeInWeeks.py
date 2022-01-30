age = input("What is your current age? ")
age = int(age)
yearsLeft = 90 - age

numDays = yearsLeft * 365
numWeeks = yearsLeft * 52
numMonths = yearsLeft * 12

print(f"You have {numDays} days, {numWeeks} weeks, and {numMonths} months left.")
