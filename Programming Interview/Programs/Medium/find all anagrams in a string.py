s= "cbaebabacd"
p= "abc"

class Solution:
    def anagram(self, s, p):
        from collections import Counter
        k = 0
        a = []
        p = list(p)
        p_count = Counter(p)
        s_count = Counter()
        x = len(p)
        for i in range(len(s)-x+1):
            s_count = Counter()
            for j in range(i, i + x):
                if s[j] in p:
                    s_count[s[j]] += 1
            if s_count == p_count:
                a.append(i)
        return a

z = Solution()
print (z.anagram(s, p))
