/*
https://leetcode.com/problems/high-five/

Runtime: 264 ms, faster than 50.00% of C# online submissions for High Five.
Memory Usage: 34.1 MB, less than 44.00% of C# online submissions for High Five.
*/

public class Solution
{
    class DecendingComparer : IComparer
    {

        public int Compare(object _x, object _y)
        {
            int x = (int)_x, y = (int)_y;
            return y.CompareTo(x);
        }
    }

    class StudentScores
    {
        public StudentScores()
        {

        }

        int id;
        ArrayList scores = new ArrayList();

        public StudentScores(int _id, int _score)
        {
            id = _id;
            scores.Add(_score);
        }
        public void addScore(int _score)
        {
            scores.Add(_score);
        }

        public int[] calculateAverage()
        {
            int[] retArray = new int[2];
            scores.Sort(new DecendingComparer());
            int range = Math.Min(5, scores.Count);
            int accum = 0;
            for (int i = 0; i < range; i++)
            {
                accum += (int)scores[i];
            }
            retArray[0] = id;
            retArray[1] = accum / range;
            return retArray;
        }


    }
    public int[][] HighFive(int[][] items)
    {
        var d = new Dictionary<int, StudentScores>();

        foreach (int[] score in items)
        {
            int studentID = score[0], studentScore = score[1];
            if (d.ContainsKey(studentID)) d[studentID].addScore(studentScore);
            else d.Add(studentID, new StudentScores(studentID, studentScore));

        }
        int stuCount = d.Values.Count;
        int[][] retItems = new int[stuCount][];

        int i = 0;
        foreach (StudentScores currStudent in d.Values)
        {
            retItems[i++] = currStudent.calculateAverage();
        }
        Array.Sort(retItems, (a, b) => a[0] - b[0]);
        return retItems;

    }
}
