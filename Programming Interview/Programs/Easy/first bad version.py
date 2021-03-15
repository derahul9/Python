isBadVersion = [1,1,1,1,0,0,1]

class Solution:
    def bad(self, isBadVersion):
        l = 0
        r = 6
        while l < r:
            mid = (l + r) // 2
            if isBadVersion[mid] == 0:
                r = mid
            elif isBadVersion[mid] == 1:
                l = mid+1
        return l+1

z = Solution()
print (z.bad(isBadVersion))