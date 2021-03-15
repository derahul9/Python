s = "foro"
t = "batr"

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if n != m:
            return False
        dic = {}
        for i in range(n):
            if s[i] in dic:
                if dic[s[i]] != t[i]:
                    return False
            elif t[i] in dic.values():
                    return False
            else:
                dic[s[i]] = t[i]
        return True

z = Solution()
print (z.isAnagram(s, t))