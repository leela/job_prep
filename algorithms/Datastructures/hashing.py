"""One of the application for hashing is building set interface. 
To Implement set interface, we need to find elements by key and we can make use of hashing to make that operation fast.

Sorting can make us find in O(log n) operations, we can make it almost constant operation using Dynamic array+hashing.
"""

import random

def modulo_hash(key, hash_table_size):
    """hash_table_size is nothing but the size of storage array.
    """
    return key % hash_table_size

def get_next_prime(n):
    pass

def universal_hash_function(key, hash_table_size, max_input_key):
    """This is not a real implementation as real implementation need to know 
        prime, a and b, whenever need to do operations on set. 
        so, (prime, a and b) are supposed to be inputs to this function instead of generating with in the function.
    """
    prime = get_next_prime(max_input_key)
    a = random.randrange(1, prime)
    b = random.randrange(0, prime)
    return (((a*key)+b) % prime ) % hash_table_size