package Fundamentals.codeSignal.heapsStacksQueues;

/*
Switching to java because the debugger is more functional with mac and linux without having to configure mono
Implement a modified stack that, in addition to using push and pop operations, allows you to find the current minimum element in the stack by using a min operation.
*/
import java.util.ArrayList;
import java.util.Collections;
import java.util.Stack;

public class q5minimumOnStack {
    public static int[] minimumOnStack(String[] operations) {
        Stack<Integer> stack = new Stack<Integer>();
        ArrayList<Integer> retArrL = new ArrayList<Integer>();
        for (String op : operations) {
            if (op.contains("push")) {
                int val = Integer.parseInt(op.split(" ")[1]);
                stack.push(val);
            } else if (op.contains("pop")) {
                stack.pop();
            } else if (op.contains("min")) {
                retArrL.add(Collections.min(stack));
            }

        }
        int[] retArr = retArrL.stream().mapToInt(x -> x).toArray();
        return retArr;
    }

    public static void main(String args[]) {
        minimumOnStack(new String[] { "push 10", "min", "push 5", "min", "push 8", "min", "pop", "min", "pop", "min" });
    }

}
