input = "01:32"

class Solution:
    def close(self, input):
        x = input.split(":")[0]
        y = input.split(":")[1]
        a = int(x)
        b = int(y)
        d = list(x) + list(y)
        o = d[0]
        p = []
        if d[0] == d[1] == d[2] == d[3]:
            return input
        for i in range(1,24*60):
            b += 1
            if b == 60:
                a += 1
                b = 0
                if a == 24:
                    a = 0
            g = list(str(a))
            h = list(str(b))
            if len(g) == 1:
                g.insert(0, '0')
            if len(h) == 1:
                h.insert(0, '0')
            m = g + h
            #print (m)
            count = 0
            for i in range(len(m)):
                if m[i]  in d:
                    count += 1
                    if count == 4:
                        return ("{:02d}:{:02d}".format(a,b))

z = Solution()
print (z.close(input))
