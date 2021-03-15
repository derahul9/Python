height = [0,1,0,2,1,0,1,3,2,1,2,1]

class Solution:
    def trap(self, height):
        n = len(height)
        ans = 0
        for i in range(len(height)):
            a = 0
            b = 0
            for j in range(i-1,-1,-1):
                a = max(a, height[j])
            for k in range(i+1, n):
                b = max(b, height[k])
            if min(a,b) - height[i] > 0:
                ans1 = min(a,b) - height[i]
                ans += ans1
        return ans

z = Solution()
print (z.trap(height))