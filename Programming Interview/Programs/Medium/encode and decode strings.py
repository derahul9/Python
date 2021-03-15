input = ["I", "am", "Vicky"]
input1 = [" "," "]

class Solution:
    def encode(self, input):
        if len(input) == 0:
            self.b = chr(300)
            return self.b
        else:
            a = (chr(300))
            self.b = chr(300).join(input)
            return self.b

    def decode(self):
        if self.b == chr(300):
            return []
        else:
            return self.b.split(chr(300))

z = Solution()
print (z.encode(input))
print (z.decode())
