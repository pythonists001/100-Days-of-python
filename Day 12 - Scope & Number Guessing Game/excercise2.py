## Modifying global scope 

enemies = "Skeleton"


def increase_enemies():
    enemies = "Zombie"
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

#############################


"""
countOfCandidates = 1
def increaseCount():
    #countOfCandidates += 1 #local variable 'countOfCandidates' referenced before assignment
    ## To use global scope and modify it's value, we need to specifically mention it.
    global countOfCandidates
    countOfCandidates += 1

    ## but it's not recommended to modify the global scope values this way
    ## creates error and confusion

    print(f"enemies inside function: {countOfCandidates}")

increaseCount()
print(f"enemies outside function: {countOfCandidates}")

"""
## better way is to
countOfCandidates = 1


def increaseCount():
    print(f"count inside function: {countOfCandidates}")
    return countOfCandidates + 5


countOfCandidates = increaseCount()
print(f"count outside function: {countOfCandidates}")
