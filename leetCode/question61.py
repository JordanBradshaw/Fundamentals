# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:  # If no head object
            return None
        # Create a new object and link to second item so we can iterate through the list
        lengthHead = ListNode(head.val, head.next)
        length = 0
        # Go through whole list to get length
        while lengthHead:
            length += 1
            lengthHead = lengthHead.next
        if length == 1:  # If only one object return the value in a node
            return ListNode(head.val)
        headPointer = ListNode(head.val, head.next)  # Create a new node so .next does lose position
        moveVal = (
            k % length
        )  # use the modulo operator for when they give you a huge number you'll only have to move the total distance
        newHead, endOfNewHead = ListNode(), ListNode()  # new objects for bounds
        for i in range(length):  # Go through the Linked nodes 0 - totalDistance-1
            if i == length - moveVal - 1 and head.next:  # if its the object where youre splitting after it
                if head.next.next:  # if theres two objects after
                    newHead = ListNode(
                        head.next.val, head.next.next
                    )  # create a new node of the next value and link it to the two away item
                else:  # Else is if its the end of the linked list Link it to starting head
                    newHead = ListNode(head.next.val, headPointer)
                # Create from the new head position it here to iterate it beyond this point via .next
                endOfNewHead = ListNode(newHead.val, newHead.next)
                head.next = None
            elif i == length - moveVal - 1 and not head.next:  # basically no switch within the nodes
                return headPointer
            elif i == length - 1:  # if its at the end of the second new head link it to the old head
                endOfNewHead.next = headPointer
            elif i >= length - moveVal:  # default to iterate to end of new head
                endOfNewHead = endOfNewHead.next
            else:
                head = head.next  # iterate to end of starting head (Which this becomes the tail)
        # Cycle Break
        cycleNode = ListNode(newHead.val, newHead.next)  # this is to remove cycles
        for i in range(length):  # You know the length of the original so iterate through your linked list
            if (
                i == length - 1
            ):  # go to the final node and set it to none this is intended for the shorter lists and we didn't set the .next pointer to none previously
                cycleNode.next = None
            else:
                cycleNode = cycleNode.next
        return newHead


temp = ListNode(1)
temp.next = ListNode(2)
temp.next.next = ListNode(3)
Solution().rotateRight(temp, 2)

# Runtime: 28 ms, faster than 97.96% of Python3 online submissions for Rotate List.
# Memory Usage: 14.2 MB, less than 57.96% of Python3 online submissions for Rotate List.
