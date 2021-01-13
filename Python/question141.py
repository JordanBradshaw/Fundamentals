# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # head is empty or doesn't exist
        if not head:
            return False
        # use a dictionary for faster search plus store the ListNode it self
        hashTable = {}
        # While there is a ListNode Object
        while head:
            # If looking in the table at the key of the ListNode Object doesn't return anything
            if not hashTable.get(head):
                # Store the value at the index of the ListNode
                hashTable[head] = head.val
            else:  # Else that means the actual node has been touched so a cycle has had to have happened
                return True
            # Go to next List Node
            head = head.next
        # If finished the loop then theres no cycles :)!
        return False


temp = ListNode(1)
temp.next = ListNode(2)
print(Solution().hasCycle(temp))

# Runtime: 40 ms, faster than 97.06% of Python3 online submissions for Linked List Cycle.
# Memory Usage: 17.1 MB, less than 85.43% of Python3 online submissions for Linked List Cycle.
