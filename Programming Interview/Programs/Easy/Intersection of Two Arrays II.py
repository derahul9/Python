nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

class Solution:
    def intersect(self, nums1, nums2):
        from collections import defaultdict
        a = defaultdict(int)
        d = []
        if len(nums1) > len(nums2):
            b = nums1
            c = nums2
        else:
            b = nums2
            c = nums1
        for elements in b:
            a[elements] += 1
        for data in c:
            if data in a:
                if a[data] > 0:
                    a[data] -= 1
                    d.append(data)
        return d

z = Solution()
print (z.intersect(nums1, nums2))