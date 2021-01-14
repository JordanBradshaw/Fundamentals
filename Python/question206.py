# Reverse a singly linked list.
from collections import deque


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not (head):
            return None
        que = deque()
        while head:
            que.append(head.val)
            head = head.next
        returnNode = ListNode(que.popleft())
        while que:
            returnNode = ListNode(que.popleft(), returnNode)
        return returnNode


# Runtime: 40 ms, faster than 33.58% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 16.5 MB, less than 25.38% of Python3 online submissions for Reverse Linked List.
