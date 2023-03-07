# Name:         Emma Bibb
# OSU Email:    bibbe@oregonstate.edu
# Course:       CS261 - Data Structures
# Assignment:   5
# Due Date:     03/06/23
# Description:  Use dynamic array from Assignment 2 to implement the complete binary tree heap
#               in which the value in each internal node is smaller than or equal to the
#               values in the children of that node.


from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return 'HEAP ' + str(heap_data)

    def add(self, node: object) -> None:
        """
        adds a new object to the MinHeap while maintaining heap property.
        """
        # set variables
        self._heap.append(node)
        child = self._heap.length() - 1
        parent = (child - 1) // 2

        # if self._heap.length() - 1 is = to 0, return
        if child == 0:
            return

        # if child heap < parent heap
        while self._heap[child] < self._heap[parent]:
            # set parent and child heap =
            temp_child = self._heap[child]
            self._heap[child] = self._heap[parent]
            self._heap[parent] = temp_child
            # set =, then -1 and / by 2
            child = parent
            parent = (child - 1) // 2

            # return if 0
            if child == 0:
                return

        # remove pass

    def is_empty(self) -> bool:
        """
        returns True if the heap is empty; otherwise, it returns False.
        """
        if self._heap.is_empty():
            return True
        else:
            return False

        # remove pass

    def get_min(self) -> object:
        """
        returns an object with the minimum key, without removing it from the heap.
        If the heap is empty, the method raises a MinHeapException.
        """
        if self._heap.is_empty():
            raise MinHeapException
        else:
            return self._heap[0]

        # remove pass

    def remove_min(self) -> object:
        """
        returns an object with the minimum key, and removes it from the heap.
        If the heap is empty, the method raises a MinHeapException.
        """
        # set variables
        min_num = self.get_min()
        self._heap[0] = self._heap[self._heap.length() - 1]
        self._heap.remove_at_index(self._heap.length() - 1)

        # call parcolate down function
        _percolate_down(self._heap, 0)

        # return min
        return min_num

        # remove pass

    def build_heap(self, da: DynamicArray) -> None:
        """
        receives a DynamicArray with objects in any order, and builds a proper MinHeap from them.
        The current content of the MinHeap is overwritten.
        """
        # set variables
        self._heap = DynamicArray(da)
        right_index = self._heap.length() - 1

        # get last indexed parent
        index = (right_index - 1) // 2

        # while index greater than -1, call percolate down
        while index > -1:
            _percolate_down(self._heap, index)
            # -1 from index
            index -= 1

        # remove pass

    def size(self) -> int:
        """
        returns the number of items currently stored in the heap
        """
        return self._heap.length()

        # remove pass

    def clear(self) -> None:
        """
        clears the contents of the heap.
        """
        self._heap = DynamicArray()

        # remove pass


def heapsort(da: DynamicArray) -> None:
    """
    Receives a DynamicArray and sorts its content in non-ascending order, using the Heapsort algorithm.
    You must sort the array in place, without creating any data structures.
    This function does not return anything.
    """
    # set variables
    right_index = da.length() - 1
    heap = MinHeap()
    heap.build_heap(da)

    # while index greater than or = to 0,
    while right_index >= 0:
        # set dynamic array index to remove min value
        da[right_index] = heap.remove_min()

        # index - 1
        right_index -= 1

    # remove pass

# It's highly recommended that you implement the following optional          #
# function for percolating elements down the MinHeap. You can call           #
# this from inside the MinHeap class. You may edit the function definition.  #

def _percolate_down(da: DynamicArray, parent: int) -> None:
    """
    percolates down the heap by swapping node with child position
    """
    # while less than dynamic array length, move position
    while (2 * parent + 1) < da.length():
        child = 2 * parent + 1

        # if parent is less than, move position
        if (2 * parent + 2) < da.length() and da[2 * parent + 2] < da[2 * parent + 1]:
            child = 2 * parent + 2

        # if child is greater than parent, return
        if da[child] > da[parent]:
            return

        # set parent = to child
        da[child], da[parent] = da[parent], da[child]
        parent = child

    # remove pass


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())

    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty() and h.is_empty() is not None:
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

    print("--------------------------")
    print("Inserting 500 into input DA:")
    da[0] = 500
    print(da)

    print("Your MinHeap:")
    print(h)
    if h.get_min() == 500:
        print("Error: input array and heap's underlying DA reference same object in memory")

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())

    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())

    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)
