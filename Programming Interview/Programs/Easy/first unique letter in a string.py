s = "loveleetcode"

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            cou = s.count(s[i])
            if cou == 1:
                return i
        return -1

z = Solution()
print (z.firstUniqChar(s))