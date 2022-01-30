print("Welcome to the Love Calculator")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

full_name = name1 + name2

t = full_name.count('t')
r = full_name.count('r')
u = full_name.count('u')
e = full_name.count('e')

true = t+r+u+e

l = full_name.count('l')
o = full_name.count('o')
v = full_name.count('v')
e = full_name.count('e')

love = l+o+v+e

love_score = int(str(true) + str(love))
if (love_score < 10) or (love_score > 90) :
  print(f"Your score is {love_score}, you go together like coke and mentos")
elif (love_score >= 40) and (love_score <= 50):
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}")
# print(f"T occurs {full_name.count('t')} times.")
# print(f"R occurs {full_name.count('r')} times.")
# print(f"U occurs {full_name.count('u')} times.")
# print(f"E occurs {full_name.count('e')} times.")

# total_count_true = full_name.count('t') + full_name.count('r') + full_name.count('u') + full_name.count('e')
# print(f"Total={total_count_true }")

# print(f"L occurs {full_name.count('l')} times.")
# print(f"O occurs {full_name.count('o')} times.")
# print(f"V occurs {full_name.count('v')} times.")
# print(f"E occurs {full_name.count('e')} times.")

# total_count_love = full_name.count('l') + full_name.count('o') + full_name.count('v') + full_name.count('e')
# print(f"Total={total_count_love }")

# print("Love Score="+str(total_count_true)+str(total_count_love))