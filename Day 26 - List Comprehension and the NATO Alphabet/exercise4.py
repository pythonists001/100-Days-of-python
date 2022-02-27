with open("Day 26 - List Comprehension and the NATO Alphabet/file1.txt", "r") as file1:
    file_1_data = file1.readlines()


with open("Day 26 - List Comprehension and the NATO Alphabet/file2.txt", "r") as file2:
    file_2_data = file2.readlines()

result = [int(num) for num in file_1_data if num in file_2_data] 
# Write your code above 👆

print(result)