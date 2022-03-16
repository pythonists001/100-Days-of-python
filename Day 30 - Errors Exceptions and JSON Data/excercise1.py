# try:
#     file = open("Day 30 - Errors Exceptions and JSON Data/a_file.txt")
#     a_dictionary = {"key" :"value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("Day 30 - Errors Exceptions and JSON Data/a_file.txt","w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error I made up")
#     # file.close()
#     # print("File was closed")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height is an error I made up.")

bmi = weight / height ** 2
print(bmi)