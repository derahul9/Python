nums = [3,0,-2,-1,1,2]
target = 0

class Sum:
    def threeSum(self, nums, target):
        a = []
        b = []
        for i in range(len(nums)-2):
            for j in range(i + 1, len(nums)-1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == target:
                        a.append(nums[i])
                        a.append(nums[j])
                        a.append(nums[k])
                        a.sort()
                        if a not in b:
                            b.append(a)
                        a = []
        return b

z = Sum()
print (z.threeSum(nums, target))

class Sum1:
    def threeSum1(self, nums, target):
        a = []
        b = []
        target = 0
        seen = {}
        for k, v in enumerate(nums):
            seen[v] = k
        for i in range(len(nums)-2):
            for j in range(i + 1, len(nums)-1):
                if target - nums[i] - nums[j] in seen:
                    if i != seen[target - nums[i] - nums[j]] and j != seen[target - nums[i] - nums[j]]:
                        a.append(nums[i])
                        a.append(nums[j])
                        a.append(target - nums[i] - nums[j])
                        a.sort()
                        if a not in b:
                            b.append(a)
                        a = []
        return b

z = Sum1()
print (z.threeSum1(nums, target))
