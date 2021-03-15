s = 'abcd'

class Solution:
    def perm(self, s):
        x = len(s)
        b = []
        a = []
        for i in range(len(s)):
            while x > i:
                a.append(s[i:x])
                x -= 1
                b.append("".join(a))
                a = []
            x = len(s)
        return b

z = Solution()
print (z.perm(s))