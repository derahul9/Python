moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]

class Solution:
    def tic(self, moves):
        a = []
        b = []
        from collections import defaultdict
        d = defaultdict(int)
        e = defaultdict(int)
        f = defaultdict(int)
        g = defaultdict(int)
        cou = 0
        for i in range(len(moves)):
            if i % 2 == 0:
                a.append(moves[i])
            else:
                b.append(moves[i])
        for j in range(len(a)):
            if d[a[j][0]] == d[a[j][1]]:
                cou += 1
                if cou == 3:
                    return ('A')
                if cou == 1:
                    if [a[j][0],a[j][1]] and [a[j][1],a[j][0]] in a:
                        return ('A')
            d[a[j][0]] += 1
            e[a[j][1]] += 1
            if d[a[j][0]] == 3 or e[a[j][1]] == 3:
                return ('A')
        for k in range(len(b)):
            if d[a[k][0]] == d[a[k][1]]:
                cou += 1
                if cou == 3:
                    return ('B')
                if cou == 1:
                    if [b[k][0],b[k][1]] and [b[k][1],b[k][0]] in b:
                        return ('B')
            f[b[k][0]] += 1
            g[b[k][1]] += 1
            if f[b[k][0]] == 3 or g[b[k][1]] == 3:
                return ('B')
        if len(moves) < 9:
            return ('Pending')
        if len(moves) == 9:
            return ('Draw')

z = Solution()
print (z.tic(moves))
