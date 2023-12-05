"""
Static Sequence
================
Assumption: 
    * Let's assume that memory accessing is Random access memory.
    * word size > log(sequence size) 
        [word size limits the memory size. ex: 32 bit word CPU, can access memory address up to 2**32]
Interface:
    build(S) - Make new DS for elements in S 
    len() - Find length of Sequence
    iter_seq() - iterate in a sequence
    get_at(index) - get value at index i
    set_at(index, value) - set value ar index i 

Solution to this interface is static array, and in Python we can use list to achive the static sequence.
(In ---Python lists are dynamic arrays---)
    
Implementation:
* Can be implemented using static array datastructure

Dynamic Sequence
================
Interface:
    * Static interface plus
    * insert_at(i, x)
    * delete_at(i)

Assumptions: 
    1. We can implement using Pointer based memory access
    2. We can also implement on top of linked list memory 
        (Linked list memory can be built on top of word-RAM memory)

Implementation:
* Can be implemented using static array datastructure
* Can be implemented using dynamic array datastructure
* Can be implemented using Linked List datastructure

NOTE: Coming to implementation in Python, as we do not have memory access in python we can use 
a list as a memory and implement. and we can use ONLY indexing as that gives us interface like
random access memory.

We got Sequence interface in Python and that uses a Dynamic array datastrcture. that is list.
"""

class StaticArraySequence:
    """Number of items does not change.

    Implementation of static and dynamic sequence interface.
    """
    def _create_memory(self, length):
        return [None for each in range(length)]

    def build(self, length=None, *values):
        """Performace - O(n)
        """
        self.length = length or len(values)
        self.memory = self._create_memory(length) #Memory allocation
        for i in range(len(values)):
            self.memory[i] = values[i]

    def len(self):
        """Performace - O(1)
        """
        return self.length

    def iter_seq(self):
        """Performace - O(n)
        """
        
        for i in range(self.length):
            print(self.memory[i])

    def get_at(self, index):
        """Performace - O(1)
        """
        return self.memory[index]

    def set_at(self, index, value):
        """Performace - O(1)
        """
        self.memory[index] = value

    def get_first(self):
        """Performace - O(1)
        """
        pass

    def get_last(self):
        """Performace - O(1)
        """
        pass

    def set_first(self, value):
        """Performace - O(1)
        """
        pass

    def set_last(self, value):
        """Performace - O(1)
        """
        pass

    def delete_at(self, i):
        """Delete and Move all items to occupy the created space.
        Performace: 
            Worstcase: O(n)
            BestCase: Ω(1)
        """
        for index in range(i, self.length-1):
            # shifting
            self.memory[i] = self.memory[i+1]
        self.length -= 1

    def insert_at(self, i, value):
        """
        Performace:
            WorstCase: O(n) + overhead of building memory again 
            BestCase: Ω()
        """
        if len(self.memory) == self.length:
            self.build_memory(self.length+1, self.memory)

        # Shifting
        for index in range(self.length, i-1, -1):
            self.memory[index+1] = self.memory[index]
        self.memory[i] = value

    def insert_first(self, value):
        """
        Performace:
            Worstcase - O(n)
        """
        pass

    def insert_last(self, value):
        """
        Performace:
            Worstcase - O(1)
        """
        pass

    def delete_first(self):
        """
        Performace:
            Worstcase - O(n)
        """
        pass

    def delete_last(self):
        """
        Performace:
            Worstcase - O(1)
        """
        pass

class Node:
    def __init__(self, value):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def get_first(self):
        return self.head

    def get_last(self):
        last_node = self.head
        while True:
            if not last_node or last_node.next:
                return last_node
            last_node = last_node.next

    def add_item(self, value):
        node = Node(value)
        last_node = self.get_last()
        if last_node is None:
            self.head = node
        else:
            last_node.next = node

    def add_items(self, *values):
        last_node = self.get_last()
        for each in values:
            node = Node(each)
            if not last_node:
                self.head = node
            else:
                last_node.next = node
            last_node = node

    def get_node_by_index(self, index):
        node = self.head
        
        for i in range(len(index)):
            if not node: return None
            node = node.next
        return node
    
class LLSequence:
    """Dynamic & static sequence interface using Linkedlist datastructure

    1. We know first element
    2. We know how to navigate from one to next
    """
    def __init__(self):
        self.llist = LinkedList()

    def build(self, *values):
        """
        Performace:
            Worstcase: O(n)
        """
        self.llist.add_items(values)

    def length(self):
        """
        Performace:
            Worstcase: O(n) [can be improved by storing length]
        """
        len = 0
        node = self.head
        if node:
            len += 1
            node = node.next
        return len

    def __iter__(self):
        """
        Performace:
            Worstcase: O(n)
        """
        node = self.head
        if node:
            yield node
            node = node.next

    def get_at(self, index):
        """
        Performace:
            Worstcase: O(n)
        """
        return self.llist.get_node_by_index(index)

    def set_at(self, index, value):
        """
        Performace:
            Worstcase: O(n)
        """
        node = self.llist.get_node_by_index(index)
        if node:
            node.value = value

    def delete_at(self, index):
        pass

    def insert_at(self, index, value):
        pass

    def insert_first(self, value):
        """
        Performace:
            Worstcase: O(1)
        """
        node = Node(value)
        node.next = self.head
        self.head = node

    def insert_last(self):
        """
        Performace:
            Worstcase: O(n) [can become O(1) with Double linked list]
        """
        pass

    def delete_first(self):
        """
        Performace:
            Worstcase: O(1)
        """
        if self.head:
            self.head = self.head.next

    def delete_last(self):
        """
        Performace:
            Worstcase: O(n) [can become O(1) with Double linked list]
        """
        pass


class DynamicArraySequence:
    """Build static and dynamic sequence interface using Dynamic array.

    NOTE: Python datatype `list` itself is a dynamic array.
    Algorithm:
    * relax the size of array constraint
    * when array becomes full and if we need to inseert, We build an array with size of constant factor larger
    """
    pass
