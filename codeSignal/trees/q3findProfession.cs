/*
Consider a special family of Engineers and Doctors. This family has the following rules:

    Everybody has two children.
    The first child of an Engineer is an Engineer and the second child is a Doctor.
    The first child of a Doctor is a Doctor and the second child is an Engineer.
    All generations of Doctors and Engineers start with an Engineer.
*/
string findProfession(int level, int pos)
{
    //                   1
    //                  2 3
    //                4 5 6 7
    //         8 9 10 11 12 13 14 15
    Stack<char> steps = new Stack<char> { };
    double nodeNum = Math.Pow(2, level - 1) - 1 + pos;
    Console.WriteLine(nodeNum);
    while (nodeNum != 1)
    {
        if (((int)nodeNum / 2) == nodeNum / 2)
        {
            nodeNum = nodeNum / 2;
            steps.Push('L');
        }
        else
        {
            nodeNum = (nodeNum - 1) / 2;
            steps.Push('R');
        }
        Console.WriteLine(nodeNum);
    }
    char child = 'E';
    foreach (char letter in steps)
    {
        Console.Write(letter);
        switch (child)
        {
            case 'E':
                if (letter == 'R')
                {
                    child = 'D';
                }
                break;
            case 'D':
                if (letter == 'R')
                {
                    child = 'E';
                }
                break;
            default:
                break;
        }
    }
    if (child == 'E')
    {
        return "Engineer";
    }
    else
    {
        return "Doctor";
    }
}
