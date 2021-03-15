version1 = "1.3.4.5"
version2 = "1.03.4.005.0"

class Version:
    def compareVersion(self, v1, v2):
        nums1 = version1.split('.')
        nums2 = version2.split('.')
        n1, n2 = len(nums1), len(nums2)

        for i in range(max(n1, n2)):
            i1 = int(nums1[i]) if i < n1 else 0
            i2 = int(nums2[i]) if i < n2 else 0
            if i1 != i2:
                return 1 if i1 > i2 else -1
        return 0

z = Version()
print (z.compareVersion(version1, version2))