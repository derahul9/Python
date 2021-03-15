s = "abc"
t = "ahbgdc"

# Remember to implement pointers, we can use while loop

class Solution:
    def Sub(self, s, t):
        l_p = len(s)
        r_p = len(t)
        l = 0
        r = 0
        while l < l_p and r < r_p:
            if s[l] == t[r]:
                l += 1
            r += 1
        return l == l_p

z = Solution()
print (z.Sub(s, t))