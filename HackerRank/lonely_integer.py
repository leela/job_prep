def lonelyinteger(seq):
    sorted_seq = sorted(seq)
    for i in range(0, len(seq), 2):
        if i+1 == len(seq) or sorted_seq[i] != sorted_seq[i+1]:
            return sorted_seq[i]