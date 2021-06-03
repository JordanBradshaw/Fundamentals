/*
1265. Print Immutable Linked List in Reverse

You are given an immutable linked list, print out all values of each node in reverse with the help of the following interface:

    ImmutableListNode: An interface of immutable linked list, you are given the head of the list.

You need to use the following functions to access the linked list (you can't access the ImmutableListNode directly):

    ImmutableListNode.printValue(): Print value of the current node.
    ImmutableListNode.getNext(): Return the next node.

The input is only given to initialize the linked list internally. You must solve this problem without modifying the linked list. In other words, you must operate the linked list using only the mentioned APIs.

Runtime: 4 ms, faster than 74.73% of C++ online submissions for Print Immutable Linked List in Reverse.
Memory Usage: 6.5 MB, less than 41.32% of C++ online submissions for Print Immutable Linked List in Reverse.
*/
#include <stack>

class Solution {
public:
    void printLinkedListInReverse(ImmutableListNode* head) {
        std::stack<ImmutableListNode*> st;
        while (head->getNext()!=NULL) {
            st.push(head);
            head=head->getNext();
        }
        st.push(head);
        while (st.size()!=0) {
            st.top()->printValue();
            st.pop();
        }
    }
};
