import java.util.Deque;
import java.util.LinkedList;
/*
https://leetcode.com/problems/swap-nodes-in-pairs/
Runtime: 0 ms, faster than 100.00% of Java online submissions for Swap Nodes in Pairs.
Memory Usage: 36.7 MB, less than 49.45% of Java online submissions for Swap Nodes in Pairs.
*/
public class q24SwapNodesinPairs {
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

    public ListNode swapPairs(ListNode head) {
        Deque<ListNode> q1 = new LinkedList<>();
        Deque<ListNode> q2 = new LinkedList<>();
        while (head != null) {
            q2.offerLast(head);
            head = head.next;
            if (head != null) {
                q1.offerLast(head);
                head = head.next;
            }
        }

        if (q1.isEmpty() && q2.isEmpty())
            return null;
        else if (q1.isEmpty())
            return q2.getFirst();
        head = q1.peekFirst();
        while (!q1.isEmpty() && !q2.isEmpty()) {
            if (q1.size() == 1 && q2.size() == 2){
                q1.pollFirst().next = q2.getFirst();
                q2.pollFirst().next = q2.getFirst();
                q2.pollFirst().next = null;
                    break;
                }
            q1.pollFirst().next = q2.getFirst();
            if (!q1.isEmpty())
                q2.pollFirst().next = q1.getFirst();
            else
                q2.pollFirst().next = null;

        }
        return head;
    }
}
