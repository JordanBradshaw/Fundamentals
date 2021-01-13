class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # head is empty or doesn't exist
        if not head:
            return None
        # use a dictionary for faster search plus store the ListNode it self
        hashTable = {}
        # While there is a ListNode Object
        while head:
            # If looking in the table at the key of the ListNode Object doesn't return anything
            if not hashTable.get(head):
                # Store the value at the index of the ListNode
                hashTable[head] = head.val
            else:  # Else that means the actual node has been touched so a cycle has had to have happened
                return head
            # Go to next List Node
            head = head.next
        # If finished the loop then theres no cycles :)!
        return None


# Runtime: 44 ms, faster than 93.43% of Python3 online submissions for Linked List Cycle II.
# Memory Usage: 17.3 MB, less than 53.59% of Python3 online submissions for Linked List Cycle II.
