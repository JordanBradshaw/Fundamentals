import java.util.ArrayList;
import java.util.List;
import java.util.Random;

/*
https://leetcode.com/problems/insert-delete-getrandom-o1/

Runtime: 260 ms, faster than 5.00% of Java online submissions for Insert Delete GetRandom O(1).
Memory Usage: 94.7 MB, less than 5.00% of Java online submissions for Insert Delete GetRandom O(1).
*/

public class q380InsertDeleteGetRandomO1 {
    class RandomizedSet {
        List<Integer> set = new ArrayList<Integer>();
        Random rng = new Random();

        /** Initialize your data structure here. */
        public RandomizedSet() {

        }

        /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
        public boolean insert(int val) {
            if (set.contains(Integer.valueOf(val)))
                return false;
            else {
                set.add(Integer.valueOf(val));
                return true;
            }

        }

        /** Removes a value from the set. Returns true if the set contained the specified element. */
        public boolean remove(int val) {
            if (set.contains(Integer.valueOf(val))) {
                set.remove(Integer.valueOf(val));
                return true;
            } else
                return false;

        }

        /** Get a random element from the set. */
        public int getRandom() {
            
            return set.get(rng.nextInt(set.size()));
        }
    }

    /**
     * Your RandomizedSet object will be instantiated and called as such:
     * RandomizedSet obj = new RandomizedSet();
     * boolean param_1 = obj.insert(val);
     * boolean param_2 = obj.remove(val);
     * int param_3 = obj.getRandom();
     */
}
