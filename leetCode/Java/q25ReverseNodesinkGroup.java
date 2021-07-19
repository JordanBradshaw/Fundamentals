import java.util.Deque;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;

/*
https://leetcode.com/problems/reverse-nodes-in-k-group/

Runtime: 3 ms, faster than 5.24% of Java online submissions for Reverse Nodes in k-Group.
Memory Usage: 39.4 MB, less than 32.53% of Java online submissions for Reverse Nodes in k-Group.
*/
public class q25ReverseNodesinkGroup {
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

  public ListNode reverseKGroup(ListNode head, int k) {
    if (k == 1)
      return head;
    List<Deque<ListNode>> listOfQs = new LinkedList<>();
    while (head != null) {
      Deque<ListNode> temp = new LinkedList<>();
      for (int i = 0; i < k; i++) {
        temp.offerFirst(head);
        head = head.next;
        if (head == null && i != k -1) {
          Iterator<ListNode> iter = temp.descendingIterator();
          Deque<ListNode> temp2 = new LinkedList<>();
          while (iter.hasNext())
            temp2.offerLast(iter.next());
          temp = temp2;
          break;
        }
        
      }
      listOfQs.add(temp);
    }
    ListNode returnNode = listOfQs.get(0).peekFirst();
    ListNode prevNode = null;
    for (Deque<ListNode> temp : listOfQs) {
      if (prevNode != null)
        prevNode.next = temp.peekFirst();
      while (!temp.isEmpty()) {
        temp.pollFirst().next = temp.peekFirst();
        if (temp.size() == 1)
          prevNode = temp.peekFirst();
      }

    }
    return returnNode;
  }
}
