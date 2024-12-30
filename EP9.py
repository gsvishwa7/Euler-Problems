def pythagorean_triple_finder(val):
    triples = [[a,b,c]
            for c in range(3,val)
            for b in range(2,c)
            for a in range(1,b)
            if a+b+c==val]
    for triple in triples:
        if triple[0]**2 + triple[1]**2 == triple[2]**2:
            product = triple[0]*triple[1]*triple[2]
            return(triple, product)
    # triples=[]
    # for c in range(3,val):
    #     for b in range(2,c):
    #         for a in range(1,b):
    #            if a+b+c==val: triples.append([a,b,c])
    #return(triples)

print(pythagorean_triple_finder(1000))
