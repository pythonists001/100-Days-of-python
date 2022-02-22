# f = open('./Day 24 - Files, Directories and Paths/my_file.txt')
# contents = f.read()
# print(contents)
# f.close()

## When we use with while opening the file, it closes as soon as the operation is over
with open("C:/Users/ArvindSingh/Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)

with open('./Day 24 - Files, Directories and Paths/new_file.txt', mode="w") as file: ##mode a as append
    file.write("This is new text")                                                   # if a file does not exist, while writing
                                                                                     # a new file will be created