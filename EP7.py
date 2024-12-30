primes = [2]
x=3

def is_prime(val):
    for i in primes:
        if val%i == 0:
            return False
    return True

if __name__ == "__main__":
    while len(primes)<10001:
        if is_prime(x):
            primes.append(x)
        x = x+2

    print(primes[-1])