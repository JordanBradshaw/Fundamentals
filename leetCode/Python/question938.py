# Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        # Invalid conditions
        if high < low:
            return 0
        elif not root:
            return 0
        treeList = []
        # INORDER TREE TRAVERSAL (Recursion)
        def inorderTree(node, passedTreeList):
            if node:
                inorderTree(node.left, passedTreeList)
                passedTreeList.append(node.val)
                inorderTree(node.right, passedTreeList)

        inorderTree(root, treeList)
        # Sort the list lowest to highest
        treeList.sort()
        # Return value starts at 0
        accumulator = 0
        for i in treeList:  # Iterate through the list
            # If the current value meets the range
            if low <= i and i <= high:
                # add it to the return value
                accumulator += i
        return accumulator


# Runtime: 256 ms, faster than 37.47% of Python3 online submissions for Range Sum of BST.
# Memory Usage: 22.3 MB, less than 38.54% of Python3 online submissions for Range Sum of BST.


temp = TreeNode(1)
temp.left = TreeNode(4)
temp.right = TreeNode(8)
temp.left.left = TreeNode(7)
Solution().rangeSumBST(temp, 1, 4)
