class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt
    def __repr__(self) -> str:
        return str(self.value)

def nth_to_last(head: Node, k: int) -> Node:
    if head is None:
        return None
    i = 0
    curr = head
    kth = head
    while curr.next:
        i+=1
        if i >= k:
            kth = kth.next
        curr = curr.next
    if i < k-1:
        return None
    return kth
    

# if __name__ == "__main__":
#     A = Node("a")
#     B = Node("b", nxt=A)
#     C = Node("c", nxt=B)
#     D = Node("d", nxt=C)
#     E = Node("e", nxt=D)
#     F = Node("f", nxt=E)
   
#     print_test = lambda x: (print(x), print(nth_to_last(F, x)))

#     print_test(0)
#     print_test(1)
#     print_test(2)
#     print_test(3)
#     print_test(4)
#     print_test(5)
#     print_test(100)
