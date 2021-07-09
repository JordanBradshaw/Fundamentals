/*
https://leetcode.com/problems/implement-trie-prefix-tree/

Needed to learn this data structure
https://www.youtube.com/watch?v=giiaIofn31A
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

    Trie() Initializes the trie object.
    void insert(String word) Inserts the string word into the trie.
    boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
    boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.



Runtime: 184 ms, faster than 96.53% of C# online submissions for Implement Trie (Prefix Tree).
Memory Usage: 49 MB, less than 59.34% of C# online submissions for Implement Trie (Prefix Tree).
*/



public class Trie
{
    private Node root;
    /** Initialize your data structure here. */
    public Trie()
    {
        root = new Node('\0');
    }

    /** Inserts a word into the trie. */
    public void Insert(string word)
    {
        Node currNode = root;
        for (int i = 0; i < word.Length; i++)
        {
            char val = word[i];
            if (currNode.children[val - 'a'] == null) currNode.children[val - 'a'] = new Node(val);
            currNode = currNode.children[val - 'a'];
        }
        currNode.isWord = true;
    }

    private Node getNode(string word)
    {
        Node currNode = root;
        for (int i = 0; i < word.Length; i++)
        {
            char val = word[i];
            if (currNode.children[val - 'a'] == null) return null;
            currNode = currNode.children[val - 'a'];
        }
        return currNode;
    }
    /** Returns if the word is in the trie. */
    public bool Search(string word)
    {
        Node node = getNode(word);
        return node != null && node.isWord;
    }

    /** Returns if there is any word in the trie that starts with the given prefix. */
    public bool StartsWith(string prefix)
    {
        return getNode(prefix) != null;
    }

    class Node
    {
        public char val;
        public bool isWord;
        public Node[] children;

        public Node(char val)
        {
            this.val = val;
            isWord = false;
            //26 Letters all lowercase
            children = new Node[26];
        }
    }
}
