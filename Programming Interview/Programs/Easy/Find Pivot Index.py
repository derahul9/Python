nums = [1,7,3,6,5,6]

class Solution:
    def Pivot(self, nums):
        sum = 0
        sum1 = 0
        a = []
        b = []
        for i in range(len(nums)):
            sum += nums[i]
            a.append(sum)
        for j in range(len(nums)-1,-1,-1):
            sum1 += nums[j]
            b.append(sum1)
        b = b[::-1]
        for k in range(len(a)):
            if a[k] == b[k]:
                return k
        return -1

z = Solution()
print(z.Pivot(nums))

class Solution(object):
    def pivotIndex(self, nums):
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1