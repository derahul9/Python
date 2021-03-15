heights = [1,1,4,2,1,3]

class Solution:
    def heightChecker(self, heights):
        cou = 0
        a = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != a[i]:
                cou += 1
        return cou

z = Solution()
print (z.heightChecker(heights))