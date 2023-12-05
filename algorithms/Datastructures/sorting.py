"""One of the application for sorting is building set interface. 
To Implement set interface, we need to find elements by key and we can make use of sorting to make that operation fast.
"""

def is_sorted(seq):
    """O(n)
    """
    for i in len(seq)-1:
        if seq[i] > seq[i+1]:
            return False
    return True

def permutations(seq):
    """
    """
    pass

def permutation_sort(seq):
    """This is one of the worst sorting algorithm. Takes \Omega(n.n!)
    """
    for each in permutations(seq):
        if is_sorted(each):
            return each
        
def selection_sort(seq):
    """This can be implemented using the sequence datastructure interface that
    we created, but using Python list for simplicity.
    * Implementing the in-place sorting algorithm. 
    * It takes O(n^2) operations

    This is the algorithm we generally use to sort books length wise
    """
    unsorted_seq_end_index = len(seq)-1
    while unsorted_seq_end_index > 0:
        max_index = None # Index of maximum value element from unsorted sub array
        for i in range(unsorted_seq_end_index+1):
            if max_index is None or seq[i] > seq[max_index]:
                max_index = i
        seq[unsorted_seq_end_index], seq[max_index] = seq[max_index], seq[unsorted_seq_end_index]
        unsorted_seq_end_index -= 1
    return seq

def insertion_sort(seq):
    """It takes O(n^2) operations

    This is the algorithm we generally use while playing cards in hand.
    """
    unsorted_seq_start_index = 1
    while unsorted_seq_start_index < len(seq):
        for i in range(unsorted_seq_start_index, 0, -1):
            if seq[i] < seq[i-1]:
                seq[i], seq[i-1] = seq[i-1], seq[i]
        unsorted_seq_start_index += 1
    return seq

def merge_sorted_arrays(seq1, seq2):
    res = []
    seq1_cindex = 0 #current index
    seq2_cindex = 0

    while seq1_cindex < len(seq1) and seq2_cindex < len(seq2):
        if seq1[seq1_cindex] < seq2[seq2_cindex]:
            res.append(seq1[seq1_cindex])
            seq1_cindex += 1
        else:
            res.append(seq2[seq2_cindex])
            seq2_cindex += 1

    if seq1_cindex < len(seq1):
        res.extend(seq1[seq1_cindex:])

    if seq2_cindex < len(seq2):
        res.extend(seq2[seq2_cindex:])
    return res

def merge_sort(seq):
    """
    Performace: \Omega(n logn)
    * When view the merge_sorted_array function calls as a tree, 
        at every level n comparisons happens  and # of levels are `log n`.
    
    """
    if len(seq) == 1:
        return seq
    left_seq = seq[:len(seq)//2]
    right_seq = seq[len(seq)//2:]
    left_sorted_seq = merge_sort(left_seq)
    right_sorted_seq = merge_sort(right_seq)
    return merge_sorted_arrays(left_sorted_seq, right_sorted_seq)

def tuple_sort(seq):
    """
    """
    pass