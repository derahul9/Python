n = 19

class Solution:
    def happy(self, n):
        def helper(n):
            n = str(n)
            x = 0
            for item in n:
                x += int(item)*int(item)
            return x

        a = []
        while n != 1 and n not in a:
            a.append(n)
            n = helper(n)
        return n == 1

z = Solution()
print (z.happy(n))