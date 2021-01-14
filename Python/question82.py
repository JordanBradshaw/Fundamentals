class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # If there is no head none return None
        if not head:
            return None
        # Preload first Value
        previousValue = head.val
        # Make a nonduplicate List && Store value 1
        nonDup = []
        nonDup.append(head.val)
        head = head.next  # Go to second item in ListNode
        while head:  # While head.next exists
            # If current val doesn't = previousValue
            if head.val != previousValue:
                nonDup.append(head.val)  # Append to the list and set previous value to current value
                previousValue = head.val
            elif (
                head.val == previousValue and nonDup and nonDup[-1] == head.val
            ):  # If they do == each other and nonDup is not empty and lastValue in nonDup == value
                nonDup.pop()  # Then pop the value from nonDup
            head = head.next  # Go to next item regardless
        if not nonDup:  # If nonDup is empty return None
            return None
        returnHead = ListNode(nonDup.pop())  # PreLoad ReturnHead
        while nonDup:  # While nonDup is not empty
            tempVal = nonDup.pop()  # popItem and store in temp Value
            returnHead = ListNode(
                tempVal, returnHead
            )  # Link Head to a new ListNode(With that temp value, And linking it to the previous node that was stored)
        print(nonDup)

        return returnHead


# Runtime: 40 ms, faster than 72.09% of Python3 online submissions for Remove Duplicates from Sorted List II.
# Memory Usage: 14.4 MB, less than 26.09% of Python3 online submissions for Remove Duplicates from Sorted List II.
