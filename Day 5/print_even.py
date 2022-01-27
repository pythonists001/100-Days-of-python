sum = 0
for n in range(1,101): ## since if it is 100, it will we upto but not including 100 hence +1 to the final number
    if n % 2 == 0:
        sum += n
print(sum)