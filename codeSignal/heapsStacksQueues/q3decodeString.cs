/*
Given an encoded string, return its corresponding decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is repeated exactly k times. Note: k is guaranteed to be a positive integer.
*/

string decodeString(string s)
{
    String pattern = @"\d+\[[a-z]+\]";
    Regex rgx = new Regex(pattern);
    Regex rgxNum = new Regex(@"\d+");
    Match match = rgx.Match(s);
    while (match.Success)
    {
        foreach (var reg in Regex.Matches(s, pattern))
        {
            string strreg = reg.ToString();
            string strnum = rgxNum.Match(strreg).ToString();
            int multiplier = Int32.Parse(strnum);
            String mathstring = strreg.Substring(strnum.Length + 1);
            Console.WriteLine(mathstring);

            mathstring = mathstring.Remove(mathstring.Length - 1, 1);
            mathstring = String.Concat(Enumerable.Repeat(mathstring, multiplier));
            Console.WriteLine(mathstring);
            s = s.Replace(strreg, mathstring);
        }
        match = rgx.Match(s);
    }
    return s;
}
