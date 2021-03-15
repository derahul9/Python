username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
timestamp = [1,2,3,4,5,6,7,8,9,10]
website = ["home","about","career","home","cart","maps","home","home","about","career"]

class Solution:
    def mostVisitedPattern(self, username, timestamp, website):
        from collections import defaultdict, Counter
        from itertools import combinations
        by_user = defaultdict(list)
        for t, u, w in sorted(zip(timestamp, username, website)):
            by_user[u].append(w)
        cnt = Counter()
        for i,v in by_user.items():
            cnt += Counter(set(combinations(v, 3)))
        print (cnt)
        return min(cnt, key=lambda P: (-cnt[P], P))

z = Solution()
print (z.mostVisitedPattern(username, timestamp, website))