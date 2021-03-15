num1 = "1789"
num2 = "15"

class Strings:
    def addStrings(self, num1, num2):
        result = []
        carry = 0
        p1 = (len(num1)) - 1
        p2 = (len(num2)) - 1
        while p1 >=0 or p2 >= 0:
            x1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            x2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
            value = (x1 + x2 + carry) % 10
            carry = (x1 + x2 + carry) // 10         # / generates float values which we don't want. We want a int value hence use //
            result.append(str(value))
            p1 = p1 - 1
            p2 = p2 - 1
        a = result[::-1]
        b = "".join(a)
        return b

z = Strings()
print (z.addStrings(num1, num2))
