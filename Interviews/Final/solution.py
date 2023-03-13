
class Node():
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next

    def __repr__(self) -> str:
        '''
        Used to allow for printing of Node instances, mostly for debugging purposes
        '''
        return "{}->{}".format(self.value, self.next)
    
def reverse_linked_list_inplace(head: Node) -> Node:
    '''
    Reverse the input linked list (starting at head) without allocating any additional memory 
    (you may use variables, but no lists, sets, dicts or other complex data structures).
    '''
    if head.next is None:
        return head
    prev, curr, nxt = None, head, None
    while curr.next is not None:

    return head

if __name__ == "__main__":
    test = lambda x: print("input:  {}\noutput: {}".format(x, reverse_linked_list_inplace(x)))
