# Note: Try to solve this task in O(n) time using O(1) additional space, where n is the number of elements in the list, since this is what you'll be asked to do during an interview.
# Given a singly linked list of integers l and an integer k, remove all elements from list l that have a valueue equal to k.

# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


from collections import deque


def removeKFromList(l, k):
    nodeQue = deque()
    if not l:
        return []
    if l and l.value != k and not l.next:
        return ListNode(l.value)
    elif l and l.value == k and not l.next:
        return []
    while l:
        if l.value != k:
            nodeQue.append(l)
        l = l.next
    if len(nodeQue) == 0:
        return None
    for i in range(len(nodeQue)):
        if i < len(nodeQue) - 2:
            nodeQue[i].next = nodeQue[i + 1]
        elif i == len(nodeQue) - 1:
            nodeQue[i].next = None
    return nodeQue[0]


tempNode = ListNode(3)
tempNode.next = ListNode(1)
tempNode.next.next = ListNode(2)
tempNode.next.next.next = ListNode(3)
tempNode.next.next.next.next = ListNode(4)
tempNode.next.next.next.next.next = ListNode(5)
removeKFromList(tempNode, 3)
