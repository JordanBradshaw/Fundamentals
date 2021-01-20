# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


from collections import deque


def isListPalindrome(l):
    valueQueue = deque()
    if not l:
        return True
    while l:
        valueQueue.append(l.value)
        l = l.next
    for i in range(len(valueQueue) // 2):
        if valueQueue[i] != valueQueue[len(valueQueue) - 1 - i]:
            return False
    return True
