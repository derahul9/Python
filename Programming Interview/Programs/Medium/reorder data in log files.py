logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

class Solution:
    def reorder(self, logs):
        a = []
        b = []
        c = []
        for data in logs:
            a.append(data.split(" "))
        for elem in a:
            if (elem[1]).isdigit():
                b.append(elem)
            else:
                c.append(elem)
        d = sorted(c, key=lambda P: (P[1], P[2]))
        f = d + b
        g = []
        for data in f:
            g.append(" ".join(data))
        return g

z = Solution()
print (z.reorder(logs))