from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        preList = []
        if lists == [] or lists == [[]]:
            return None
        for currentNode in lists:
            tempSmallList = []
            if not currentNode:
                tempSmallList.append(None)
                continue
            else:
                tempSmallList.append(currentNode.val)
                while currentNode.next != None:
                    currentNode = currentNode.next
                    tempSmallList.append(currentNode.val)
                preList.append(tempSmallList)
        postList = []
        for item in preList:
            postList += item
        postList.sort()
        try:
            returnNode = ListNode(postList[0])
        except IndexError:
            return None
        nextNode = returnNode
        for i in range(1, len(postList)):
            nextNode.next = ListNode(postList[i])
            nextNode = nextNode.next
        return returnNode


item1 = ListNode(1)
item1.next = ListNode(4)
item1.next.next = ListNode(5)

item2 = ListNode(1)
item2.next = ListNode(3)
item2.next.next = ListNode(4)

item3 = ListNode(2)
item3.next = ListNode(6)

pushList = [item1, item2, item3]
sol = Solution()
sol.mergeKLists(pushList)

# Runtime: 100 ms, faster than 74.87% of Python3 online submissions for Merge k Sorted Lists.
# Memory Usage: 19.5 MB, less than 6.28% of Python3 online submissions for Merge k Sorted Lists.
