names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

import random
random_pick = names[random.randint(0,len(names)-1)]

print(f"{random_pick} is going to buy the meal today!")

## We can also use choice as well to get random value from list\
##  random.choice(names) ##sometimes gives repeated instance