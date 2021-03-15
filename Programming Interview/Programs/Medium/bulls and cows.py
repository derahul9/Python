secret = "1123"
guess = "0111"

class Solution:
    def bulls(self, s, g):
        from collections import Counter
        h = Counter(s)
        bulls = cows = 0
        for i in range(len(s)):
            if s[i] == g[i]:
                bulls += 1
                h[s[i]] -= 1
        for i in range(len(g)):
            if g[i] in s:
                if g[i] != s[i]:
                    if h[g[i]] > 0:
                        cows += 1
                        h[g[i]] -= 1
        return "{}A{}B".format(bulls, cows)

z = Solution()
print (z.bulls(secret, guess))


