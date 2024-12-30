import EP7

def sums_of_primes(val):
    for x in range(3, val, 2):
        if EP7.is_prime(x):
            EP7.primes.append(x)
    return(sum(EP7.primes))

print(sums_of_primes(2000000))