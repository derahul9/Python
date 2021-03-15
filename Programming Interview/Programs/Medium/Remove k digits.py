num = "1432219"
k = 3

class Solution:
    def remove(self, num, k):
        if k == len(num):
            return "0"
        a = []
        l = len(num)
        for digit in num:
            while k and a and a[-1] > digit:
                a.pop()
                k -= 1
            a.append(digit)
        if k > 0:
            a = a[:-k]
            return "".join(a).lstrip('0') or "0"
        else:
            return "".join(a).lstrip('0') or "0"


z = Solution()
print (z.remove(num, k))



