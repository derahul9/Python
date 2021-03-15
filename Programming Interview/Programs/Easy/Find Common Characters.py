inp = ["bbddabab","cbcddbdd","bbcadcab","dabcacad","cddcacbc","ccbdbcba","cbddaccc","accdcdbb"]

class Solution(object):
    def commonChars(self, A):
        from collections import defaultdict
        mapfirst = defaultdict(int)

        for c in A[0]:
            mapfirst[c] += 1
        for s in A:
            tempmap = defaultdict(int)
            for c in s:
                tempmap[c] += 1

            for c in mapfirst:
                mapfirst[c] = min(mapfirst[c], tempmap[c])
        ans = []
        for c in mapfirst:
            for i in range(mapfirst[c]):
                ans.append(c)
        return ans

z= Solution()
print (z.commonChars(inp))