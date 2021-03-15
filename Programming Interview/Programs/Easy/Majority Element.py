nums = [2,2,1,1,1,2,2]

class Solution:
    def firstUniqChar(self, s):
        for i in range(len(s)):
            cou = s.count(s[i])
            if cou > (len(s) // 2):
                return s[i]

z = Solution()
print (z.firstUniqChar(nums))

class Solution1:
    def firstUniqChar1(self, s):
        from collections import defaultdict
        x = defaultdict(int)
        for elements in nums:
            x[elements] += 1
        x = sorted(x.items(), key=lambda item: item[1], reverse=True)
        return x[0][0]

z = Solution1()
print (z.firstUniqChar1(nums))