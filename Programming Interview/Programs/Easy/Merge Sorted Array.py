nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

class Sorted():
    def mergeSorted(self, nums1, nums2):
        nums3 = (nums1 + nums2)
        a = len(nums3)
        for i in range(a - 1):
            for j in range (i + 1, a):
                if nums3[i] > nums3[j]:
                    nums3[i], nums3[j]  = nums3[j], nums3[i]
        return nums3

z = Sorted()
print (z.mergeSorted(nums1, nums2))

class Sorted1():
    def mergeSorted1(self, nums1, m, nums2, n):
        nums1_copy = nums1[:m]
        nums1 = []
        p1 = 0
        p2 = 0
        while p1 < m and p2 < n:
            if nums1_copy[p1] < nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1
        if p1 < m:
            nums1[p1 + p2:] = nums1_copy[p1:]
        if p2 < n:
            nums1[p1 + p2:] = nums2[p2:]
        return nums1

z = Sorted1()
print (z.mergeSorted1(nums1, m, nums2, n))