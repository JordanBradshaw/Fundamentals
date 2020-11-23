#Difficulty: Easy
#Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.
#Example 1:
#Input: l1 = [1,2,4], l2 = [1,3,4]
#Output: [1,1,2,3,4,4]
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        nodeHead = ListNode()
        current = nodeHead
        if l1 is [] and l2 is []:
            return []
        while (l1 and l2):
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        if l1:
            current.next = l1
        elif l2:
            current.next = l2
        return nodeHead.next

#Runtime: 32 ms, faster than 90.25% of Python3 online submissions for Merge Two Sorted Lists.
#Memory Usage: 14.3 MB, less than 8.66% of Python3 online submissions for Merge Two Sorted Lists.