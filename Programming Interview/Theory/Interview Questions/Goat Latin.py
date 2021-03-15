s = "The quick brown fox jumped over the lazy dog"

class Solution:
    def goat(self, s):
        x = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        a = s.split(" ")
        b = []
        for i in range(len(a)):
            n = 0
            if a[i][0] in x:
                    y = a[i] + "ma"
                    while n <= i:
                        y = y + "a"
                        n += 1
                    b.append(y)
            if a[i][0] not in x:
                    y = a[i][1:len(a[i])] + a[i][0] + "ma"
                    while n <= i:
                        y = y + "a"
                        n += 1
                    b.append(y)
        return " ".join(b)

z = Solution()
print (z.goat(s))