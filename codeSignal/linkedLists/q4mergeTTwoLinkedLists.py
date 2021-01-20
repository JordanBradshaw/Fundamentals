# Note: Your solution should have O(l1.length + l2.length) time complexity, since this is what you will be asked to accomplish in an interview.
#
# Given two singly linked lists sorted in non-decreasing order, your task is to merge them. In other words, return a singly linked list, also sorted in non-decreasing order, that contains the elements from both original lists.

# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


from collections import deque


def mergeTwoLinkedLists(l1, l2):
    quickQue = deque()
    if not l1 and not l2:
        return None
    elif not l1:
        return l2
    elif not l2:
        return l1

    while l1:
        quickQue.append(l1.value)
        l1 = l1.next
    while l2:
        quickQue.append(l2.value)
        l2 = l2.next
    returnNode = runnerNode = None
    for value in sorted(quickQue):
        if not returnNode:
            returnNode = runnerNode = ListNode(value)
        else:
            runnerNode.next = ListNode(value)
            runnerNode = runnerNode.next
    return returnNode
