nums1 = [-2147483647]
nums2 = [-2,1,-3,2,4,-1,2,1,-5,4]

class Sub:
    def maxSub(self, nums):
        n = len(nums)
        carry = max_value = nums[0]
        for i in range(1, n):
            x = carry + nums[i]
            y = nums[i]
            carry = max(y, x)
            max_value = max(max_value, carry)
        return max_value

z = Sub()
print (z.maxSub(nums2))