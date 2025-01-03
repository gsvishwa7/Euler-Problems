
# I found the SymPy package, but maybe we try understanding the SE answer
# given in this link https://stackoverflow.com/questions/43683012/divisors-of-a-number-how-can-i-improve-this-code-to-find-the-number-of-divisors
# and also here https://stackoverflow.com/questions/171765/what-is-the-best-way-to-get-all-the-divisors-of-a-number

###################################
from math import sqrt
from functools import lru_cache, reduce
from collections import Counter
from itertools import product


MUL = int.__mul__


def prime_factors(n):
    'Map prime factors to their multiplicity for n'
    d = _divs(n)
    #print(d)
    if d[-1] == d:
        print("AAAAAAHHHHH")
    d = [] if d == [n] else d
    #(d[:-1] if d[-1] == d else d)
    pf = Counter(d)
    return dict(pf)

@lru_cache(maxsize=None)
def _divs(n):
    'Memoized recursive function returning prime factors of n as a list'
    for i in range(2, int(sqrt(n)+1)):
        d, m  = divmod(n, i)
        if not m:
            return [i] + _divs(d)
    return [n]


def proper_divs(n):
    '''Return the set of proper divisors of n.'''
    pf = prime_factors(n)
    pfactors, occurrences = pf.keys(), pf.values()
    multiplicities = product(*(range(oc + 1) for oc in occurrences))
    divs = {reduce(MUL, (pf**m for pf, m in zip(pfactors, multis)), 1)
            for multis in multiplicities}
    try:
        divs.remove(n)
    except KeyError:
        pass
    return divs or ({1} if n != 1 else set())



if __name__ == '__main__':
    rangemax = 20000
    
    print([proper_divs(n) for n in range(1, 11)])
    print(*max(((n, len(proper_divs(n))) for n in range(1, 20001)), key=lambda pd: pd[1]))
##############################
