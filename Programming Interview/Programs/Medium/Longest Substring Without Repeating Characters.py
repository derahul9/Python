s = "abcabcbb"

class Solution:
    def sub(self, s):
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        else:
            a = []
            b = []
            ans = 0
            for i in range(len(s) - 1):
                a.append(s[i])
                for j in range(i + 1, len(s)):
                    if s[j] in a:
                        break
                    if s[j] not in a:
                        a.append(s[j])
                count = len(a)
                ans = max(count, ans)
                a = []
            return ans

z = Solution()
print (z.sub(s))

