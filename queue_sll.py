# Name:         Emma Bibb
# OSU Email:    bibbe@oregonstate.edu
# Course:       CS261 - Data Structures
# Assignment:   3 - Linked List and ADT Implementation
# Due Date:     02/13/2023
# Description:  implement the Stack and Queue ADTs, but by using the Singly Linked Nodes


from SLNode import SLNode


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Initialize new queue with head and tail nodes
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = None
        self._tail = None

    def __str__(self):
        """
        Return content of queue in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'QUEUE ['
        if not self.is_empty():
            node = self._head
            out = out + str(node.value)
            node = node.next
            while node:
                out = out + ' -> ' + str(node.value)
                node = node.next
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    def enqueue(self, value: object) -> None:
        """
        adds a new value to the end of the queue
        """

        current = SLNode(value)

        # creates tail and head
        # if tail = None, set to current
        if self._tail is None:
            self._tail = current
            self._head = current

        # else, = next to current
        else:
            self._tail.next = current
            self._tail = current

        # remove pass

    def dequeue(self) -> object:
        """
        removes and returns the value from the beginning of the queue
        If the queue is empty, the method raises a custom “QueueException
        """

        # if size = 0, raise exception
        if self.size() == 0:
            raise QueueException

        # removes value
        remove = self._head.value

        # returns to beginning
        self._head = self._head.next
        return remove

       # remove pass

    def front(self) -> object:
        """
        returns the value of the front element of the queue without removing it
        If the queue is empty, the method raises a custom “QueueException
        """

        # if size = 0, raise exception
        if self.size() == 0:
            raise QueueException

        # return value in front
        return self._head.value

    # remove pass


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# enqueue example 1")
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)

    print("\n# dequeue example 1")
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(6):
        try:
            print(q.dequeue())
        except Exception as e:
            print("No elements in queue", type(e))

    print('\n#front example 1')
    q = Queue()
    print(q)
    for value in ['A', 'B', 'C', 'D']:
        try:
            print(q.front())
        except Exception as e:
            print("No elements in queue", type(e))
        q.enqueue(value)
    print(q)
