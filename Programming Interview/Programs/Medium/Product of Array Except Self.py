s = [1,2,3,4]

class Product:
    def arrayProduct(self, s):
        a = []
        b = 1
        for i in range(len(s)):
            b = b * s[i]
        for i in range(t):
            a.append(int(b / s[i]))
        return a

z = Product()
print (z.arrayProduct(s))

class Product1:
    def arrayProduct1(self, s):
        t = len(s)
        a = []
        b = 1
        c = 1
        for i in range(t):
            for l in range(0, i):
                b = b * s[l]
            for r in range(i +1, t):
                c = c * s[r]
            a.append(int(b * c))
            b = 1
            c = 1
        return a

z = Product1()
print (z.arrayProduct1(s))
