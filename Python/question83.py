# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from collections import deque


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        previousValue = head.val
        nonDup = []
        nonDup.append(head.val)
        head = head.next
        while head:
            print(head.val)
            if head.val != previousValue:
                nonDup.append(head.val)
                previousValue = head.val
            head = head.next
        print(nonDup)
        returnHead = ListNode(nonDup.pop())
        while nonDup:
            tempVal = nonDup.pop()
            returnHead = ListNode(tempVal, returnHead)
        print(nonDup)

        return returnHead


temp = ListNode(1)
temp = ListNode(1, temp)
temp = ListNode(2, temp)
temp = ListNode(3, temp)
temp = ListNode(3, temp)
Solution().deleteDuplicates(temp)
# Runtime: 52 ms, faster than 11.64% of Python3 online submissions for Remove Duplicates from Sorted List.
# Memory Usage: 14.4 MB, less than 24.88% of Python3 online submissions for Remove Duplicates from Sorted List.
