a = "1111"
b = "0010"

class Binary:
    def addBinary(a, b):
        x = (int(a, 2))
        y = (int(b, 2))
        z = (x + y)
        return (bin(z))

class Binary1:
    def addBinary1(self, a, b):
        x, y = int(a, 2), int(b, 2)
        print (x)
        print (y)
        while y != 0:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)

class Binary2:
    def addBinary2(self, a, b):
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)

        carry = 0
        ans = []
        for i in range(n-1, -1, -1):
            if a[i] =="1":
                carry += 1
            if b[i] == "1":
                carry += 1

            if carry % 2 == 0:
                ans.append("0")
            else:
                ans.append("1")

            carry //= 2

        if carry == 1:
            ans.append("1")
        ans.reverse()
        return "".join(ans)

z = Binary1()
print (z.addBinary1(a, b))