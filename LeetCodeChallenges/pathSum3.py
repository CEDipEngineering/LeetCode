from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        self.cumSum = {0:1}
        self.pathSumRecursive(root, targetSum, 0)
        return self.count
            
    def pathSumRecursive(self, root, target_sum, current_sum):
        if root is None: return

        # Add root
        current_sum += root.val
        # Check if it added a new path that adds up to the target, then update the counter
        self.count += self.cumSum.get(current_sum - target_sum, 0)
        self.cumSum[current_sum] = self.cumSum.get(current_sum, 0) + 1

        # Check left and right
        self.pathSumRecursive(root.left, target_sum, current_sum)
        self.pathSumRecursive(root.right, target_sum, current_sum)

        # Remove this value when going back up
        self.cumSum[current_sum] -= 1

if __name__ == "__main__":
    S = Solution()
    
    r = TreeNode(10)
    r.left = TreeNode(5)
    r.left.left = TreeNode(3)
    r.left.left.left = TreeNode(3)
    r.right = TreeNode(-3)
    r.left.right = TreeNode(2)
    r.left.right.right = TreeNode(1)
    r.left.left.right = TreeNode(-2)
    r.right.right = TreeNode(11)

    '''
         10
       5     -3
     3   2     11
    3 -2  1
    '''

    print(S.pathSum(r, 8))