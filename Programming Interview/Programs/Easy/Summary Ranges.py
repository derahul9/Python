nums = [0,1,2,4,5,7]

class Solution:
    def summaryRanges(self, nums):
        ans = []
        if not nums:
            return []
        if len(nums) == 1:
            ans.append(str(nums[0]))
        a = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                if i == len(nums)-1:
                    ans.append("{}->{}".format(a,nums[i]))
                continue
            if nums[i] - nums[i-1] > 1:
                if nums[i-1] == a:
                    ans.append(str(a))
                    a = nums[i]
                    if i == len(nums)-1:
                        ans.append(str(nums[i]))
                else:
                    ans.append("{}->{}".format(a,nums[i-1]))
                    a = nums[i]
                    if i == len(nums)-1:
                        ans.append(str(nums[i]))
        return ans

z = Solution()
print (z.summaryRanges(nums))