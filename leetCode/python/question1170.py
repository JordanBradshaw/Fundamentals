# Let's define a function f(s) over a non-empty string s, which calculates the frequency of the smallest character in s. For example, if s = "dcce" then f(s) = 2 because the smallest character is "c" and its frequency is 2.
# Now, given string arrays queries and words, return an integer array answer, where each answer[i] is the number of words such that f(queries[i]) < f(W), where W is a word in words.
from typing import List


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        frequency = []
        for item in queries:
            frequencyCount = 0
            for item2 in words:
                if item.count(min(item)) < item2.count(min(item2)):
                    frequencyCount += 1
            frequency.append(frequencyCount)
        return frequency


solution = Solution()
print(solution.numSmallerByFrequency(["bbb", "cc"], ["a", "aa", "aaa", "aaaa"]))

# Runtime: 6652 ms, faster than 5.10% of Python3 online submissions for Compare Strings by Frequency of the Smallest Character.
# Memory Usage: 14.7 MB, less than 70.46% of Python3 online submissions for Compare Strings by Frequency of the Smallest Character.
