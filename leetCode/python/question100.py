# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if stepsAnalyze(p, q) == False:
            return False
        qList = returnList(q)
        pList = returnList(p)
        if len(pList) == len(qList):
            for x, y in zip(pList, qList):
                if x != y:
                    return False
        else:
            return False
        return True


def stepsAnalyze(p, q):
    pSteps, qSteps = [], []

    def stepInorder(currentRoot, currentSteps):
        if currentRoot:
            if currentRoot.left != None:
                currentSteps.append("L")
            stepInorder(currentRoot.left, currentSteps)
            if currentRoot.right != None:
                currentSteps.append("R")
            stepInorder(currentRoot.right, currentSteps)

    stepInorder(p, pSteps)
    stepInorder(q, qSteps)
    return pSteps == qSteps


def returnList(root):
    tempList = []

    def printInorder(root):
        if root:
            printInorder(root.left)
            tempList.append(root.val)
            printInorder(root.right)

    printInorder(root)
    return tempList


# Runtime: 32 ms, faster than 54.68% of Python3 online submissions for Same Tree.
# Memory Usage: 14.4 MB, less than 23.41% of Python3 online submissions for Same Tree.
