st = "aabbccccc"

class Solution:
    def reorg(self, st):
        a = []
        c = []
        n = len(st)
        t = set(st)
        for elements in t:
            a.append([elements, st.count(elements)])
        b = sorted(a, key= lambda P: P[1])
        m = len(b)
        if b[m-1][1] > ((n+1) // 2):
            return ""
        else:
            ans = [None] * n
            print (b)
            for elements in b:
                while elements[1] > 0:
                    c.append(elements[0])
                    elements[1] -= 1
            print (c)
            ans[::2], ans[1::2] = c[n // 2:], c[:n // 2]
            return "".join(ans)

z = Solution()
print (z.reorg(st))

