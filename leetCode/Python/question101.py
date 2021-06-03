# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        leftList = []
        rightList = []
        if not root:
            return True
        try:
            if root.left.val != root.right.val:
                return False
        except AttributeError:
            pass

        def findLeft(node: TreeNode, lL: List):
            if node:
                if node.left == None and node.right != None:
                    lL.append(None)
                findLeft(node.left, lL)
                lL.append(node.val)
                if node.right == None and node.left != None:
                    lL.append(None)
                findLeft(node.right, lL)

        def findRight(node: TreeNode, rL: List):
            if node:
                if node.right == None and node.left != None:
                    rL.append(None)
                findRight(node.right, rL)
                rL.append(node.val)
                if node.left == None and node.right != None:
                    rL.append(None)
                findRight(node.left, rL)

        findLeft(root.left, leftList)
        findRight(root.right, rightList)
        if leftList == rightList:
            return True
        else:
            return False


# Runtime: 32 ms, faster than 81.65% of Python3 online submissions for Symmetric Tree.
# Memory Usage: 14.6 MB, less than 10.67% of Python3 online submissions for Symmetric Tree.
