s2 = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]

s1 = "leetcode"
wordDict1 = ["leet", "code"]

class Solution:
    def word_break(self, s, wordDict):
        if s in wordDict:
            return True
        for i in range(len(s)):
            if s[:i] in wordDict:
                print (s[:i])
                return self.word_break(s[i:], wordDict)
        return False


z = Solution()
print (z.word_break(s2, wordDict))

