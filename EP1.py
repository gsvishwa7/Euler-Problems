#Hi.
     
#Find the sum of all the multiples of 3 or 5 below 1000.
sum=0
num_accepted = []

for x in range(1000):
    if x%3 == 0 or x%5 == 0:
        sum = sum + x
        num_accepted.append(x)
print(sum)
