s = "deeedbbcccbdaa"
k = 3

class Solution:
    def removeDuplicates(self, s, k):
        size = len(s)
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            elif s[i] != s[i - 1]:
                count = 1

            if count == k:
                s = s.replace(s[i - k + 1:i + 1], "")
                return self.removeDuplicates(s, k)
        return s

z = Solution()
print (z.removeDuplicates(s, k))