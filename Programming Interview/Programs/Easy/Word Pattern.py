pattern = "abba"
s = "dog cat cat dog"

class Solution:
    def wordPattern(self, pattern, s):
        from collections import defaultdict
        arr = defaultdict(str)
        s = s.split(" ")
        if len(pattern) != len(s):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in arr:
                if s[i] in arr.values():
                    return False
                else:
                    arr[pattern[i]] = s[i]
            if pattern[i] in arr:
                if arr[pattern[i]] != s[i]:
                    return False
        return True

z = Solution()
print (z.wordPattern(pattern,s))