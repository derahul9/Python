items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]

class Solution:
    def highFive(self, items):
        items.sort(key = lambda P: (P[0], P[1]), reverse= True)
        from collections import defaultdict
        a = []
        b = []
        d = defaultdict(int)
        e = defaultdict(int)
        for elements in items:
            if e[elements[0]] is None or e[elements[0]] < 5:
                d[elements[0]] += elements[1]
                e[elements[0]] += 1
        for k, v in d.items():
            a.append(k)
            a.append(v // 5)
            b.append(a)
            a = []
        c = sorted(b, key= lambda P:(P[0], P[1]))
        return c

z = Solution()
print (z.highFive(items))