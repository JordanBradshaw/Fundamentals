# Given the root of a binary tree, return the leftmost value in the last row of the tree.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        # Create empty list for inorderTree
        inOrderList = []

        # Recursive function to get inorder list also passing row and each time a child is called upped the row by 1
        def inOrderTraverse(node, row):
            if node:
                inOrderTraverse(node.left, row + 1)
                inOrderList.append((node.val, row))
                inOrderTraverse(node.right, row + 1)

        # Starting point (root value, row 0)
        inOrderTraverse(root, 0)
        # This worst case return which would be root, row 0
        returnTuple = (root.val, 0)
        # iterate through the list of (value,row)
        for (x, y) in inOrderList:
            # if the row is greater than the stored (also not >= because we want the left most value and its in order)
            if y > returnTuple[1]:
                # store it
                returnTuple = (x, y)
        # return the first value of the stored tuple
        return returnTuple[0]


# Runtime: 48 ms, faster than 38.15% of Python3 online submissions for Find Bottom Left Tree Value.
# Memory Usage: 17.8 MB, less than 7.75% of Python3 online submissions for Find Bottom Left Tree Value.


temp = TreeNode(1)
temp.left = TreeNode(4)
temp.right = TreeNode(8)
temp.left.left = TreeNode(7)
Solution().findBottomLeftValue(temp)
