a = "abcd"
b = "cdabcdab"

class Solution:
    def stringMatch(self, a, b):
        q = (len(b) +1) // (len(a) -1)
        for i in range(q):
            if b in a*(q+i):
                return q + i
        return -1

z = Solution()
print (z.stringMatch(a, b))


