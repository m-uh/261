# Name:         Emma Bibb
# OSU Email:    bibbe@oregonstate.edu
# Course:       CS261 - Data Structures
# Assignment:   3 - Linked List and ADT Implementation
# Due Date:     02/13/2023
# Description:  implement the Stack and Queue ADTs, but by using the Singly Linked Nodes


from SLNode import SLNode


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Stack:
    def __init__(self) -> None:
        """
        Initialize new stack with head node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = None

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'STACK ['
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
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    def push(self, value: object) -> None:
        """
        adds a new element to the top of the stack
        """

        # creates node
        current = SLNode(value)
        current.next = self._head

        # assigns
        self._head = current

        # remove pass

    def pop(self) -> object:
        """
        method removes the top element from the stack and returns its value
        If the stack is empty, the method raises a custom ???StackException???
        """

        # if size = 0, raise exception
        if self.size() == 0:
            raise StackException

        # remove value
        remove = self._head.value
        self._head = self._head.next

        # return value
        return remove

        # remove pass

    def top(self) -> object:
        """
        returns the value of the top element of the stack without removing it.
        If the stack is empty, the method raises a custom ???StackException???
        """

        # if size = 0, raise exception
        if self.size() == 0:
            raise StackException

        # return value on top of stack
        return self._head.value

        # remove pass

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# push example 1")
    s = Stack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)

    print("\n# pop example 1")
    s = Stack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))

    print("\n# top example 1")
    s = Stack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)
