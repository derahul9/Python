s = "babad"

class Solution:
    def pal(self, s):
        m = ""
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                if len(m) > j - i:
                    break
                elif s[i:j] == s[i:j][::-1]:
                    m = s[i:j]
                    print (m)
                    break
        return m

z = Solution()
print (z.pal(s))