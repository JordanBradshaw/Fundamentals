/*
You have two arrays of strings, words and parts. Return an array that contains the strings from words, modified so that any occurrences of the substrings from parts are surrounded by square brackets [], following these guidelines:

If several parts substrings occur in one string in words, choose the longest one. If there is still more than one such part, then choose the one that appears first in the string.
*/




string[] findSubstrings(string[] words, string[] parts)
{
    List<string> returnWords = new List<string> { };
    Dictionary<int, List<string>> arraySearch = new Dictionary<int, List<string>> { };
    foreach (string part in parts)
    {
        try
        {
            arraySearch[part.Length].Add(part);
        }
        catch (KeyNotFoundException)
        {
            arraySearch[part.Length] = new List<string>() { part };
        }
    }
    string findLowestIndex(List<string> currIndexList, string currIndexWord)
    {
        string returnWord = null;
        int lowestIndex = currIndexWord.Length;
        foreach (string currIndex in currIndexList)
        {
            if (currIndexWord.IndexOf(currIndex) != -1)
            {
                if (currIndexWord.IndexOf(currIndex) < lowestIndex)
                {
                    returnWord = currIndex; lowestIndex = currIndexWord.IndexOf(currIndex);
                }
            }
        }
        return returnWord;
    }
    int[] keyList = arraySearch.Keys.OrderByDescending(x => x).ToArray();
    string[] orderedParts = parts.OrderByDescending(x => x.Length).ToArray();


    foreach (string curWord in words)
    {
        bool replacedString = false;
        foreach (int key in keyList)
        {
            string minPart = findLowestIndex(arraySearch[key], curWord);
            if (minPart != null)
            {
                var regex = new Regex(Regex.Escape(minPart));
                returnWords.Add((string)regex.Replace(curWord, "[" + minPart + "]", 1));
                replacedString = true;
                break;
            }
        }
        if (!replacedString)
        {
            returnWords.Add(curWord);
        }
    }
    /*
    foreach (string curWord in words){
        bool replacedString = false;
        foreach (string curPart in orderedParts){
            if (curWord.Contains(curPart)){
                string minPart = findLowestIndex(arraySearch[curPart.Length],curWord);
                var regex = new Regex(Regex.Escape(minPart));
                returnWords.Add((string)regex.Replace(curWord, "["+minPart+"]", 1));
                replacedString = true;
                break;
            }
        }
        if (!replacedString){
            returnWords.Add(curWord);
        }
    }*/

foreach (KeyValuePair<int, List<string>> kvp in arraySearch)
    {
        Console.WriteLine("Key = {0}, Value = {1}", kvp.Key, kvp.Value);
        foreach (string word in kvp.Value)
        {
            Console.WriteLine(word);
        }
        //Console.WriteLine(key);
    }/*
    foreach (int temp in keyList){
        Console.WriteLine(temp);
    }*/

    return returnWords.ToArray();
}
