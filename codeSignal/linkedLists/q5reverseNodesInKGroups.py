# Note: Your solution should have O(n) time complexity, where n is the number of elements in l, and O(1) additional space complexity, since this is what you would be asked to accomplish in an interview.
#
# Given a linked list l, reverse its nodes k at a time and return the modified list. k is a positive integer that is less than or equal to the length of l. If the number of nodes in the linked list is not a multiple of k, then the nodes that are left out at the end should remain as-is.
#
# You may not alter the values in the nodes - only the nodes themselves can be changed.


# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


from collections import deque


#
def reverseNodesInKGroups(l, k):
    def shiftArray(startingIndex):
        for i in range(k // 2):
            tempValue = dQue[i + startingIndex]
            dQue[i + startingIndex] = dQue[startingIndex + k - i - 1]
            dQue[startingIndex + k - i - 1] = tempValue

    dQue = deque()
    while l:
        dQue.append(l.value)
        l = l.next
    extra = len(dQue) % k
    for ind in range(0, len(dQue) - extra, k):
        print(ind)
        shiftArray(ind)
    print(dQue)
    returnNode = runnerNode = None
    for value in dQue:
        if not returnNode:
            returnNode = runnerNode = ListNode(value)
        else:
            runnerNode.next = ListNode(value)
            runnerNode = runnerNode.next
    return returnNode


tempNode = ListNode(1)
tempNode.next = ListNode(2)
tempNode.next.next = ListNode(3)
tempNode.next.next.next = ListNode(4)
tempNode.next.next.next.next = ListNode(5)

reverseNodesInKGroups(tempNode, 2)
