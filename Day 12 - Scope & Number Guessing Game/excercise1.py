############### Scope ################

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

## Local Scope
"""
## Local Scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
print(potion_strength) ## not accessible
"""

## Global Scope

player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()
print(player_health)

## There is no Block scope
"""
A variable inside a function is only available inside that function, 
but variables inside a conditional statement outside of any function will be available to consequent program lines.
"""