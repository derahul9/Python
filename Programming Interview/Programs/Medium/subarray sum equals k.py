nums = [1,1,1]
k = 2

class Solution:
    def sum(self, nums, k):
        count = 0
        for i in range(0, len(nums)):
            sum = nums[i]
            if k - sum == 0:
                count += 1
            for j in range(i + 1, len(nums)):
                sum += nums[j]
                if k - sum == 0:
                    count += 1
        return count

z = Solution()
print (z.sum(nums, k))
