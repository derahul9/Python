s = "anagram"
t = "nagaram"

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = defaultdict(int)
        b = defaultdict(int)
        for i in s:
            a[i] += 1
        for j in t:
            b[j] += 1
        return a == b

z = Solution()
print (z.isAnagram(s, t))