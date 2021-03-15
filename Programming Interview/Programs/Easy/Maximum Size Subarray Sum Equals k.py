nums = [-2, -1, 2, 1]
k = 1

class Solution:
    def subarr(self, nums, k):
        ans = 0
        if len(nums) == 0:
            return 0
        count = 0
        for i in range(len(nums) - 1):
            x = nums[i]
            for j in range(i + 1, len(nums)):
                x = x + nums[j]
                if x == k:
                    count = (j - i) + 1
            x = 0
            ans = max(count, ans)
        return ans

z = Solution()
print (z.subarr(nums, k))


