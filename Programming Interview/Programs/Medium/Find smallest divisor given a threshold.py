nums = [1,2,5,9]
threshold = 6

class Solution:
    def threshold(self, nums, threshold):
        sum = 0
        for j in range(1, max(nums) + 1):
            for i in range(len(nums)):
                dividend = nums[i] // j
                if nums[i] % j > 0:
                    dividend += 1
                sum += dividend
            if sum <= threshold:
                    return j
            sum = 0
            dividend = 0

z = Solution()
print (z.threshold(nums, threshold))
