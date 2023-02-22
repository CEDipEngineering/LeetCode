from typing import List, Tuple
import math

# Do not modify the classes below
class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, representation: str):
        '''
        representation: List of values representing a binary tree. The left and right
        children of the ith element are 2i+1 and 2i+2, respectively.
        '''
        if not representation:
            self.root = None
            return
        nodes = []
        for i, value in enumerate(representation):
            node = None
            if value is not None:
                node = TreeNode(value)
                if i > 0:
                    if i % 2 == 1:
                        parent = nodes[(i - 1) // 2]
                        parent.left = node
                    else:
                        parent = nodes[(i - 2) // 2]
                        parent.right = node
            nodes.append(node)
        self.root = nodes[0]


class LinkedListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class LinkedList:
    def __init__(self, values):
        self.root = None
        if not values:
            return
        prev = None
        for value in values:
            node = LinkedListNode(value)
            if prev:
                prev.next = node
            if self.root is None:
                self.root = node
            prev = node


# Implement the functions below

def list_sum(l: List[int]) -> int:
    if len(l) == 0: return 0
    k = l.pop()
    return k + list_sum(l)


def digit_sum(n: int) -> int:
    i = n//10
    j = n%10
    if j == n: return j
    return j + digit_sum(i)


def tree_sum(root: TreeNode) -> int:
    if root is None:
        return 0
    return root.value + tree_sum(root.left) + tree_sum(root.right)


def tree_max(root: TreeNode) -> int:
    if root is None:
        return -math.inf
    return max(root.value, tree_max(root.right), tree_max(root.left))


def k_combinations(l: List[int], k: int) -> List[List[int]]:
    if k == 0:
        return [[]] # return single digit combinations
    comb_bases = []

    for i in range(len(l)):
        elem = l[i]
        remList = l[(i + 1):]
        for e in k_combinations(remList, k-1):
            comb_bases.append([elem, *e])
    return comb_bases

def all_strictly_increasing_sequences(k: int, n: int, **kwargs) -> List[List[int]]:
    return []


def create_pattern(n: int) -> List[int]:
    return []


def find_middle(head: LinkedListNode) -> LinkedListNode:
    # Don't change this function
    return find_middle_rec(head)[1]


def find_middle_rec(head: LinkedListNode, n: int=0) -> Tuple[int, LinkedListNode]:
    # Hint: n will be used to count nodes from left to right and
    # the number returned by the function will be used to count the nodes from right to left
    # TODO: Implement this function
    return None, 0

# if __name__ == "__main__":
#     print(k_combinations([1,2,3], 1))
#     print(k_combinations([1,2,3], 2))
#     print(k_combinations([1,2,3], 3))