"""
Set Interface:
container:
    build(X)
    len()
static:
    find(K)
dynamic:
    insert(x)
    delete(k)
order:
    iter_ord()
    find_min()
    find_max()
    find_next(k)
    find_prev(k)

* `x` is an object with key(student_id) and information(like student_name, sage, sbranch).
* `k` stands for key and is used to find value(x object).

Assumption:
* Keys are integers

Sol1
----
* Implement using static/dynamic array(unordered array) data structure that we created for sequence interface.
    - All the operations take O(n) and is not really efficient.   
* As unordered array is inefficient, we can try implementing ordered array
     (Instead of input order, we store them sorted by key)
"""
import sequence

class UnorderedArray:
    """This is very inefficient datastructure as all the operations take linear time to complete.
    """
    def __init__(self):
        self.array =  None

    def build(self, X):
        self.array = sequence.DynamicArraySequence()
        self.array.build(*X)
        
    def find(self, k):
        for each in self.array:
            if each.key == k:
                return each
    # TODO: Implement remaining interface

class OrderedArray:
    """This Ordered array perform better than Unordered array.
    To build ordered array we need to take O(nlogn), but all other search operations perform better on Ordered Array.
    insert and delete take O(n) time.
    """
    pass