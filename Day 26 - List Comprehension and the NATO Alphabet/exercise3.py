dbl = [n*2 for n in range(1,5)]
print(dbl)

names = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
short_names = [n for n in names if len(n) < 5]
print(short_names)

upper_name = [n.upper() for n in names if len(n) > 5]
print(upper_name)

#print even numbers
numbers = [5, 4, 3, 28, 89, 21, 74]
result = [num for num in numbers if num%2 == 0]
print(result)

## print prime numbers
result_prime = [x for x in range(2, 100)
     if all(x % y != 0 for y in range(2, x))]

print(result_prime)