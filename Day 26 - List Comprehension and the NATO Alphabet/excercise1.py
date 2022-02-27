numbers = [1,2,3]
# new_numbers = [new_item for item in list]
new_numbers = [n+1 for n in numbers]
new_squares = [n*n for n in numbers]
print(new_numbers)
print(new_squares)

name = "Arvind"
new_list = [letter for letter in name]
print(new_list)