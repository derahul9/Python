num1 = "123"
num2 = "456"

class Solution:
    def mul(self, num1, num2):
        a = []
        for data in num1:
            a.append(ord(str(data)) - ord(str(0)))
        n = len(a)
        b = 0
        for i in range(n):
            b += a[n-1-i] * 10**i
        d = []
        for data1 in num2:
            d.append(ord(str(data1)) - ord(str(0)))
        m = len(d)
        t = 0
        for j in range(m):
            t += d[m-1-j] * 10**j
        mul = 0
        for k in range(max(b,t)):
            mul += min(b,t)
        return mul

z = Solution()
print (z.mul(num1, num2))