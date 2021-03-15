nums = [1,2,3]

class Solution(object):
    def minMoves(self, nums):
        c = 0
        nums.sort()
        for i in range(len(nums)-1, -1, -1):
            c += nums[i] - nums[0]
        return c

z = Solution()
print (z.minMoves(nums))