n = 5

class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        curr = self.climbStairs(n-1) + self.climbStairs(n-2)
        return curr

z = Solution()
print (z.climbStairs(n))