# What is the largest prime factor of 600851475143?

current_factor = 2
quotient = 600851475143

while current_factor <= quotient:
    if quotient%current_factor == 0:
        quotient = quotient/current_factor
        if quotient == 1:
            break
        else: current_factor = 2
    else: current_factor = current_factor + 1

print(current_factor)