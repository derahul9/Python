nums = [1,2,4,4,3,3,0,9,2,3]
k = 3

class Solution:
    def diff(self, nums, k):
        a = []
        b = []
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    a.append([nums[i], nums[j]])
        for i in range(len(a)):
            if [a[i][0],a[i][1]] not in b and [a[i][1],a[i][0]] not in b:
                b.append(a[i])
        return len(b)

z = Solution()
print (z.diff(nums, k))

class Solution1:
    def diff1(self, nums, k):
        count = 0
        from collections import defaultdict
        a = defaultdict(int)
        for values in nums:
            a[values] += 1
        #print (a)
        for i, v in a.items():
            if k - i == i:
                if a[i] > 1:
                    count += 1
            elif k + i in a:
                count += 1
        return count

z = Solution1()
print (z.diff1(nums, k))