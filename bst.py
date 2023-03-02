
import random
from queue_and_stack import Queue, Stack


class BSTNode:
    """
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        """
        Initialize a new BST node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value   # to store node's data
        self.left = None     # pointer to root of left subtree
        self.right = None    # pointer to root of right subtree

    def __str__(self) -> str:
        """
        Override string method
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'BST Node: {}'.format(self.value)


class BST:
    """
    Binary Search Tree class
    """

    def __init__(self, start_tree=None) -> None:
        """
        Initialize new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Override string method; display in pre-order
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self._root, values)
        return "BST pre-order { " + ", ".join(values) + " }"

    def _str_helper(self, node: BSTNode, values: []) -> None:
        """
        Helper method for __str__. Does pre-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if not node:
            return
        values.append(str(node.value))
        self._str_helper(node.left, values)
        self._str_helper(node.right, values)

    def get_root(self) -> BSTNode:
        """
        Return root of tree, or None if empty
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._root

    def is_valid_bst(self) -> bool:
        """
        Perform pre-order traversal of the tree.
        Return False if nodes don't adhere to the bst ordering property.

        This is intended to be a troubleshooting method to help find any
        inconsistencies in the tree after the add() or remove() operations.
        A return of True from this method doesn't guarantee that your tree
        is the 'correct' result, just that it satisfies bst ordering.

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        stack = Stack()
        stack.push(self._root)
        while not stack.is_empty():
            node = stack.pop()
            if node:
                if node.left and node.left.value >= node.value:
                    return False
                if node.right and node.right.value < node.value:
                    return False
                stack.push(node.right)
                stack.push(node.left)
        return True

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
        adds a new value to the tree.
        Duplicate values are allowed.
        If a node with that value is already in the tree,
        the new value should be added to the right subtree of that node.
        """
        current = self._root

        # if empty tree, root becomes value
        if self._root is None:
            self._root = BSTNode(value)
            return

        while current is not None:
            # if value is less, go left
            if value < current.value:
                if current.left is None:
                    current.left = BSTNode(value)
                    return
                else:
                    current = current.left
            # if value is greater, go right
            else:
                if current.right is None:
                    current.right = BSTNode(value)
                    return
                else:
                    current = current.right

            # remove pass

    def remove(self, value: object) -> bool:
        """
         removes a value from the tree.
         The method returns True if the value is removed.
         Otherwise, it returns False
        """
        # return False if no value found
        if not self.contains(value):
            return False

        # return and call helper
        self._root = self.remove_helper(self._root, value)
        return True

    def remove_helper(self, first_node, cue):
        """
        remove helper function
        """
        # look for root, return none
        if not first_node:
            return None

        # if, 'cue' is < value, then look for cue on left tree
        if first_node.value > cue:
            first_node.left = self.remove_helper(first_node.left, cue)

        # else if 'cue' is > value, then look for cue on right tree
        elif first_node.value < cue:
            first_node.right = self.remove_helper(first_node.right, cue)

        # if neither, then cue = value
        else:
            # if first_node (root) is on left and right
            if first_node.left and first_node.right:

                # and if right tree has far left node
                if first_node.right.left:
                    # set =
                    farleft = first_node.right.left
                    # and set the farthest left root
                    leftroot = first_node.right

                    # find parent of far left node
                    while farleft.left:
                        farleft = farleft.left
                        leftroot = leftroot.left

                    # far left parent = left node
                    leftroot.left = farleft.right
                    # left far left and right far left = left root and right root, and replace left
                    farleft.left, farleft.right = first_node.left, first_node.right
                    first_node = farleft

                # else no left tree, replace right instead
                else:
                    first_node.right.left = first_node.left
                    first_node = first_node.right

            # if only one subnode on left, still replace
            elif first_node.left:
                first_node = first_node.left
                # if only one subnode on right, still replace
            elif first_node.right:
                first_node = first_node.right
                # else, = None
            else:
                first_node = None

        return first_node

    def contains(self, value: object) -> bool:
        """
        returns True if the value is in the tree.
        Otherwise, it returns False.
        If the tree is empty, the method should return False
        """
        current = self._root

        # find value
        while current is not None:
            # if value is less, go left
            if value < current.value:
                current = current.left
                # if value is greater than or equal, go right
                # if found, return true
            elif value >= current.value:
                if current.value == value:
                    return True
                current = current.right
        # else return false
        return False

        # remove pass

    def inorder_traversal(self) -> Queue:
        """
        will perform an inorder traversal of the tree, and return a Queue object that
        contains the values of the visited nodes, in the order they were visited.
        If the tree is empty, the method returns an empty Queue
        """
        que = Queue()

        # call helper function
        self.inorder_traversal_helper(self._root, que)
        return que

        # remove pass

    def inorder_traversal_helper(self, current, que):
        """
        helper function for inorder_traversal
        """
        # return once finished
        if current is None:
            return
        else:
            # add/get value and move current
            self.inorder_traversal_helper(current.left, que)
            que.enqueue(current.value)
            self.inorder_traversal_helper(current.right, que)

    def find_min(self) -> object:
        """
         returns the lowest value in the tree.
         If the tree is empty, the method should return None
        """
        # if no root, return none
        if not self._root:
            return None
        # call and return helper function
        return self.find_min_helper(self._root)

        # remove pass

    def find_min_helper(self, current: BSTNode):
        """
        helper function for find_min
        """
        # if not current value, return
        if not current.left:
            return current.value

        return self.find_min_helper(current.left)

    def find_max(self) -> object:
        """
        returns the highest value in the tree.
        If the tree is empty, the method should return None.
        """
        # not root, return none
        if not self._root:
            return None

        # call and return helper function
        return self.find_max_helper(self._root)

        # remove pass

    def find_max_helper(self, current: BSTNode):
        """
        helper function for find_max
        """
        # if not current value, return
        if not current.right:
            return current.value

        return self.find_max_helper(current.right)

    def is_empty(self) -> bool:
        """
        returns True if the tree is empty.
        Otherwise, it returns False.
        """
        # if tree is empty, return true
        if self._root is None:
            return True
        # else, return false
        else:
            return False

        # remove pass

    def make_empty(self) -> None:
        """
        removes all nodes from the tree.
        """
        self._root = None

        # remove pass

    def find_remove_node(self, value):
        """
        Returns the node to be removed and its parent
        """
        # if root
        if self._root.value == value:
            return self._root, None
        current = self._root
        remove_node = None
        remove_parent = None
        while current is not None:
            # finds node to be removed
            if current.value == value:
                remove_node = current
                break
            # finds parent of node to be removed
            if current.right is not None:
                if current.right.value == value:
                    remove_parent = current
            if current.left is not None:
                if current.left.value == value:
                    remove_parent = current
            # iterates to value
            if value < current.value:
                current = current.left
            else:
                current = current.right
        return remove_node, remove_parent


# ------------------- BASIC TESTING -----------------------------------------

if __name__ == '__main__':

    print("\nPDF - method add() example 1")
    print("----------------------------")
    test_cases = (
        (1, 2, 3),
        (3, 2, 1),
        (1, 3, 2),
        (3, 1, 2),
    )
    for case in test_cases:
        tree = BST(case)
        print(tree)

    print("\nPDF - method add() example 2")
    print("----------------------------")
    test_cases = (
        (10, 20, 30, 40, 50),
        (10, 20, 30, 50, 40),
        (30, 20, 10, 5, 1),
        (30, 20, 10, 1, 5),
        (5, 4, 6, 3, 7, 2, 8),
        (range(0, 30, 3)),
        (range(0, 31, 3)),
        (range(0, 34, 3)),
        (range(10, -10, -2)),
        ('A', 'B', 'C', 'D', 'E'),
        (1, 1, 1, 1),
    )
    for case in test_cases:
        tree = BST(case)
        print('INPUT  :', case)
        print('RESULT :', tree)

    print("\nPDF - method add() example 3")
    print("----------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = BST()
        for value in case:
            tree.add(value)
        if not tree.is_valid_bst():
            raise Exception("PROBLEM WITH ADD OPERATION")
    print('add() stress test finished')

    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    test_cases = (
        ((1, 2, 3), 1),
        ((1, 2, 3), 2),
        ((1, 2, 3), 3),
        ((50, 40, 60, 30, 70, 20, 80, 45), 0),
        ((50, 40, 60, 30, 70, 20, 80, 45), 45),
        ((50, 40, 60, 30, 70, 20, 80, 45), 40),
        ((50, 40, 60, 30, 70, 20, 80, 45), 30),
    )
    for case, del_value in test_cases:
        tree = BST(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    test_cases = (
        ((50, 40, 60, 30, 70, 20, 80, 45), 20),
        ((50, 40, 60, 30, 70, 20, 80, 15), 40),
        ((50, 40, 60, 30, 70, 20, 80, 35), 20),
        ((50, 40, 60, 30, 70, 20, 80, 25), 40),
    )
    for case, del_value in test_cases:
        tree = BST(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    case = range(-9, 16, 2)
    tree = BST(case)
    for del_value in case:
        print('INPUT  :', tree, del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 4")
    print("-------------------------------")
    case = range(0, 34, 3)
    tree = BST(case)
    for _ in case[:-2]:
        root_value = tree.get_root().value
        print('INPUT  :', tree, root_value)
        tree.remove(root_value)
        if not tree.is_valid_bst():
            raise Exception("PROBLEM WITH REMOVE OPERATION")
        print('RESULT :', tree)

    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = BST([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = BST()
    print(tree.contains(0))

    print("\nPDF - method inorder_traversal() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.inorder_traversal())

    print("\nPDF - method inorder_traversal() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree.inorder_traversal())

    print("\nPDF - method find_min() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_min() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_max() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method find_max() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method is_empty() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method is_empty() example 2")
    print("---------------------------------")
    tree = BST()
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method make_empty() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)

    print("\nPDF - method make_empty() example 2")
    print("---------------------------------")
    tree = BST()
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)
