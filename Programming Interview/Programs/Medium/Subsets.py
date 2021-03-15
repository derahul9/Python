nums = [1,2,3,4, 5, 6]

class Solution:
    def subsets(self, nums):
        from itertools import combinations
        a = []
        a.append([])
        for i in range(1, len(nums) +1):
            x = (combinations(nums, i))
            for items in x:
                a.append(list(items))
        return a

z = Solution()
print (z.subsets(nums))
