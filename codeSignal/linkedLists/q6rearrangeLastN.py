# Note: Try to solve this task in O(list size) time using O(1) additional space, since this is what you'll be asked during an interview.
#
# Given a singly linked list of integers l and a non-negative integer n, move the last n list nodes to the beginning of the linked list.

# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def rearrangeLastN(l, n):
    lRunner = lNewHead = lNewMid = l
    counter = 0
    if not l:
        return None
    if not l.next:
        return l
    while lRunner:
        lRunner = lRunner.next
        counter += 1
    n = n % counter
    if n == 0:
        return l
    for i in range(counter):
        if i <= counter - n - 1:
            if i == counter - n - 1:
                tempNode = l
                l = l.next
                lNewHead = l
                tempNode.next = None
            else:
                l = l.next
        else:
            if i == counter - 1:
                l.next = lNewMid
            else:
                l = l.next
    return lNewHead


tempNode = ListNode(1)
tempNode.next = ListNode(2)
tempNode.next.next = ListNode(3)
tempNode.next.next.next = ListNode(4)
tempNode.next.next.next.next = ListNode(5)

rearrangeLastN(tempNode, 2)
