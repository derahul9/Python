s = "ADDD"

class Number:
    def titleToNumber(self, s):
        result = 0
        n = len(s)
        for i in range(n):
            last_element = n - 1 - i
            t = int(ord(s[last_element])) - 64
            result = (result) + (t * (26**i))
        return result

z = Number()
print (z.titleToNumber(s))

