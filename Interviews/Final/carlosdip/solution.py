
class Node():
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next

    def __str__(self) -> str:
        '''
        Used to allow for printing of Node instances, mostly for debugging purposes
        '''
        if self.next is None:
            return "{}".format(self.value)
        return "{}->{}".format(self.value, self.next)


    def __repr__(self) -> str:
        return str(self)
    
def reverse_linked_list_inplace(head: Node) -> Node:
    '''
    Reverse the input linked list (starting at head) without allocating any additional memory 
    (you may use variables, but no lists, sets, dicts or other complex data structures).
    '''
    if head.next is None:
        return head
    prev, curr, nxt = None, head, None
    while curr is not None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

if __name__ == "__main__":
    E = Node(5, None)
    D = Node(4, E)
    C = Node(3, D)
    B = Node(2, C)
    A = Node(1, B)

    # List:
    # 1 -> 2 -> 3 -> 4 -> 5 -> None

    test = lambda x: print("input:  {}\noutput: {}".format(str(x), reverse_linked_list_inplace(x)))

    test(A) # Outputs 5 -> 4 -> 3 -> 2 -> 1

    test(C) # Outputs 1 -> 2 -> 3

    test(E) # Outputs 3 -> 4 -> 5