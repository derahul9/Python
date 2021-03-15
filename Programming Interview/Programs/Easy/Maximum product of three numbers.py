nums = [-1,-2,-3]

class Solution:
    def maximumProduct(self, nums):
        ans = 1
        nums.sort(reverse=True)
        ans1 = nums[0]
        for i in range(len(nums)-2,len(nums)):
            ans1 *= nums[i]
        for i in range(0,3):
            ans *= nums[i]
        return max(ans,ans1)

z = Solution()
print (z.maximumProduct(nums))
