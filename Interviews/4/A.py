class TreeNode:
    def __init__(self, value=None, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def in_order_succ(node: TreeNode) -> TreeNode:
    if node is None:
        return None
    if node.right is not None:
        curr = node.right
        while curr.left is not None:
            curr = curr.left
        return curr
    else:
        curr = node
        if curr.parent == None:
            return None
        while curr.parent.left != curr:
            curr = curr.parent
            if curr.parent == None:
                return None
            if curr.parent.left == curr:
                return curr.parent
        return curr.parent
        
if __name__ == "__main__":
    A = TreeNode("a")
    B = TreeNode("b")
    C = TreeNode("c")
    A.left = C
    A.right = B
    B.parent = A
    C.parent = A
    print(in_order_succ(C).value)