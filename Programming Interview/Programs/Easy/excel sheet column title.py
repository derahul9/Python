n = 701

class Title:
    def convertToTitle(self, n):
        R = []
        while n > 0:
            m = (n - 1) % 26
            n = (n - 1) // 26
            R.append(chr(m + 65))
        a = R[::-1]
        return "".join(a)

z = Title()
print (z.convertToTitle(n))


