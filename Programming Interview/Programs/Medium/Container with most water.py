height = [1,8,6,2,5,4,8,3,7]

class Solution:
    def most(self, height):
        length = 0
        breadth = 0
        ans = float('-inf')
        for i in range(len(height)):
            for j in range(len(height)-1,i,-1):
                breadth = j - i
                length = min(height[i], height[j])
                area = length*breadth
                ans = max(area, ans)
        if ans != float('-inf'):
            return ans
        else:
            return 0

z = Solution()
print (z.most(height))