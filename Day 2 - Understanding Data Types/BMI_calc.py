height = input("Enter your height in meters: ")
weight = input("Enter your weight in kilograms: ")

w_int = int(weight)
h_float = float(height)

bmi = round(w_int / (h_float ** 2))
bmi = w_int // (h_float ** 2)
print(bmi)
