package Fundamentals.codeSignal.treesAdvanced;

import java.util.HashMap;

/*
Of course a tree height can be calculated as the length of the longest path in it (it is also called tree diameter). So, now you have a task you need to solve, so go ahead!
*/
public class q1treeDiameter {
    public static class TreeBuilder {
        HashMap<Integer, Node> nodeDict = new HashMap<Integer, Node>();

        public class Node {
            int val;
            Node parent, l, r = null;

            public Node(int val) {
                this.val = val;
            }
        }
        public Node findRoot(){
            for(Node currNode: this.nodeDict.values()){
                if (currNode.parent == null) return currNode;
            }
            return null;
        }

        public int recursiveDiameter(Node node) {
            int lDiameter = 0;
            int rDiameter = 0;
            if (node == null)
                return -1;
            /*if (node.l == null && node.r == null)
                return 0;*/
            int lHeight = height(node.l);
            int rHeight = height(node.r);
            lDiameter = 1 + recursiveDiameter(node.l);
            rDiameter = 1 + recursiveDiameter(node.r);
            if (lHeight == -1 && rHeight == -1){
                return 0;
            }
            return Math.max(Math.max(rDiameter, lDiameter), (lHeight == -1 || rHeight == -1) ? lHeight + rHeight + 1 : lHeight + rHeight + 1);
        }

        public int height(Node n) {
            if (n == null)
                return -1;
            return 1 + Math.max(height(n.l), height(n.r));
        }

        public Node dictInsert(int val) {
            Node currNode = new Node(val);
            this.nodeDict.put(val, currNode);
            return currNode;
        }

        public void linkParentToChild(Node nodePar, Node nodeChi) {
            if (nodePar.l == null)
                nodePar.l = nodeChi;
            else
                nodePar.r = nodeChi;
            nodeChi.parent = nodePar;
        }

        public void insert(int[] twoVal) {
            Node nodePar, nodeChi;
            if (this.nodeDict.containsKey(twoVal[0]))
                nodePar = this.nodeDict.get(twoVal[0]);
            else
                nodePar = dictInsert(twoVal[0]);
            if (this.nodeDict.containsKey(twoVal[1]))
                nodeChi = this.nodeDict.get(twoVal[1]);
            else
                nodeChi = dictInsert(twoVal[1]);
            linkParentToChild(nodePar, nodeChi);
        }

    }

    public static int treeDiameter(int n, int[][] tree) {
        if (n==1) return 0;
        TreeBuilder builder = new TreeBuilder();
        for (int[] currPair : tree) {
            builder.insert(currPair);
        }
        return builder.recursiveDiameter(builder.findRoot());
        //return 0;
    }

    public static void main(String[] args) {
        //int[][] input = { {2, 5}, {5, 7},{ 5, 1 }, { 1, 9 }, { 1, 0 }, { 7, 6 }, { 6, 3 }, { 3, 8 }, { 8, 4 } };
        //int[][] input = {{1,2}, {2,0}};
        int[][] input = {{1,3}, {7,3}, {5,3}, {8,7}, {4,1}, {2,3}, {9,4}, {0,8}, {6,8}};
        treeDiameter(input.length, input);
    }

}
