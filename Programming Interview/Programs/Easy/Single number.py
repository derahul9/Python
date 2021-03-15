'''Defaultdict is a container like dictionaries present in the module collections. Defaultdict is a sub-class of the dict class that returns a dictionary-like object.
The functionality of both dictionaries and defualtdict are almost same except for the fact that defualtdict never raises a KeyError.
It provides a default value for the key that does not exists.'''

nums = [4,1,2,1,2]

class Solution:
    def singleNumber(self, nums):
        from collections import defaultdict
        a = defaultdict(int)
        for i in nums:
            a[i] += 1

        for i in a:
            if a[i] == 1:
                return i

z = Solution()
print (z.singleNumber(nums))

class Solution1:
    def singleNumber1(self, nums):
        for item in nums:
            if nums.count(item) == 1:
                return item

z = Solution1()
print (z.singleNumber1(nums))