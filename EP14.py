def odd_operation(val):
    return 3*val + 1

def even_operation(val):
    return int(val/2)

def CSequence(num):
    x=num
    seq = [num]
    while x != 1:
        if x%2:
            x=odd_operation(x)
            seq.append(x)
        else:
            x=even_operation(x)
            seq.append(x)    
    return(seq)

def sequence_generator(upper_bound):
    all_sequences = dict((y, CSequence(y)) for y in range(1,upper_bound,2))
    #for x in range(1,upper_bound,2):
    return all_sequences   


sequence_generator(1000000)