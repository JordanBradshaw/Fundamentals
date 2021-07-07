package Fundamentals.leetCode.Java;

import java.util.Deque;
import java.util.LinkedList;
import java.util.Stack;

/*
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Runtime: 1 ms, faster than 17.61% of Java online submissions for Remove Nth Node From End of List.
Memory Usage: 37.3 MB, less than 24.44% of Java online submissions for Remove Nth Node From End of List.
*/
public class q19RemoveNthNodeFromEndofList {
    //Definition for singly-linked list.
    public class ListNode {
        int val;
        ListNode next;

        ListNode() {
        }

        ListNode(int val) {
            this.val = val;
        }

        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
    }

    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode temp = head;
        Stack<ListNode> s = new Stack<ListNode>();
        while (temp != null) {
            s.add(temp);
            temp = temp.next;
        }
        if (n == s.size())
            head = head.next;
        else if (n == 1) {
            s.pop();
            s.pop().next = null;
        } else if (n == 2) {
            ListNode holder = s.pop();
            s.pop();
            s.pop().next = holder;
        } else {
            Deque<ListNode> q = new LinkedList<ListNode>();
            int counter = 1;
            while (counter++ != n - 1) {
                s.pop();
            }
            for (int i = 0; i < 3; i++) {
                q.addFirst(s.pop());
            }
            q.pollFirst().next = q.pollLast();
        }
        //temp.next = temp.next.next;
        return head;
    }

}
