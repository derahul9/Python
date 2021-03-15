v1 = [1,2]
v2 = [3,4,5,6]

class Zig():
    def zag(self, v1, v2):
        p1 = 0
        p2 = 0
        a = []
        while p1 < len(v1) and p2 < len(v2):
                a.append(v1[p1])
                p1 += 1
                a.append(v2[p2])
                p2 += 1
        if p1 < len(v1):
            a[p1 + p2:] = v1[p1:]
        if p2 < len(v2):
            a[p1 + p2:] = v2[p2:]
        return a

z = Zig()
print (z.zag(v1, v2))