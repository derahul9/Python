nums = [0,1,3,50,75]
lower = 0
upper = 99

class Solution:
    def range(self, nums, lower, upper):
        a = []
        l = len(nums)
        nums.insert(l, upper+ 1)
        nums.insert(0, lower- 1)
        l = len(nums)
        #print (nums)
        for i in range(1,l):
            if abs(nums[i] - nums[i-1]) > 1:
                if nums[i-1] + 1 == nums[i] - 1:
                    a.append(nums[i-1] + 1)
                else:
                    a.append("{}-->{}".format((nums[i-1] + 1),(nums[i]) - 1))
        return a

z = Solution()
print (z.range(nums, lower, upper))

