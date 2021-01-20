# Given a singly linked list, determine if it is a palindrome.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return False
        numArray = []
        while head:
            numArray.append(str(head.val))
            head = head.next
        firstString = "".join(numArray)
        numArray.reverse()
        secondString = "".join(numArray)
        return firstString == secondString


# Runtime: 76 ms, faster than 35.60% of Python3 online submissions for Palindrome Linked List.
# Memory Usage: 27.6 MB, less than 9.73% of Python3 online submissions for Palindrome Linked List.
