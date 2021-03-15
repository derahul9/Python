nums = [18,6,7,15,3]
target = 9

# self is used as the first parameter when using function within a class.
# enumerate is used to acces both index and value in a list
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number
# len function gives the length of a list

class Sum:
    def twoSum(self, nums, target):
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    if nums[i] + nums[j] == target:
                        return i, j

class Sum1:
    def twoSum1(self, nums, target):
        seen = {}
        for i, v in enumerate(nums):
            remaining = target - v
            if remaining in seen:
                return [seen[remaining], i]
            seen[v] = i
            print (seen)
        return []

z = Sum1()
print (z.twoSum1(nums, target))


