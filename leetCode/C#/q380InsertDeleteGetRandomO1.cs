/*
https://leetcode.com/problems/insert-delete-getrandom-o1/

Runtime: 456 ms, faster than 23.64% of C# online submissions for Insert Delete GetRandom O(1).
Memory Usage: 86.4 MB, less than 33.33% of C# online submissions for Insert Delete GetRandom O(1).
*/

public class RandomizedSet {
    HashSet<int> set = new HashSet<int>();
    Random rnd = new Random();
    /** Initialize your data structure here. */
    public RandomizedSet() {
        
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    public bool Insert(int val) {
        if (set.Contains(val)) return false;
        else{
            set.Add(val);
            return true;
        }
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    public bool Remove(int val) {
        if (set.Contains(val)) {
            set.Remove(val);
            return true;
        }
        else return false;
        
    }
    
    /** Get a random element from the set. */
    public int GetRandom() {
        return set.ElementAt(rnd.Next(set.Count));
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * bool param_1 = obj.Insert(val);
 * bool param_2 = obj.Remove(val);
 * int param_3 = obj.GetRandom();
 */
