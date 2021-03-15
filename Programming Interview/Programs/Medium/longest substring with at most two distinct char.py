input = "eceba"
k = 2

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s, k):
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        else:
            a = []
            ans = 0
            for i in range(len(s) - 1):
                y = 1
                a.append(s[i])
                for j in range(i+1, len(s)):
                    if s[j] not in a and y == 2:
                        break
                    elif s[j] not in a and y < k:
                        a.append(s[j])
                        y += 1
                    elif s[j] in a:
                        a.append(s[j])
                ans = max(ans, len(a))
                a = []
            return ans

#z = Solution()
#print (z.lengthOfLongestSubstringTwoDistinct(input, k))

class Solution1:
    def lengthOfLongestSubstringTwoDistinct1(self, s: str) -> int:
        a = []
        b = []
        s = list(s)
        for i in range(len(s)-1):
            a.append(s[i])
            cou = 1
            print (a)
            for j in range(1+i, len(s)):
                print (s[j])
                if s[j] in a:
                    a.append(s[j])
                if s[j] not in a and cou < 3:
                    a.append(s[j])
                    cou += 1
            b.append("".join(a))
            a = []
        c = sorted(b, key = lambda P: len(P), reverse=True)
        return len(c[0])

z = Solution1()
print (z.lengthOfLongestSubstringTwoDistinct1(input))