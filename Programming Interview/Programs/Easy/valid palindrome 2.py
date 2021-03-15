input = "abc"

class Solution:
    def pal(self, input):
        if input[::1] == input[::-1]:
                return True
        for i in range(len(input)):
            x = (input[:i] + input[i+1:])
            if x[::1] == x[::-1]:
                return True
        return False

z = Solution()
print (z.pal(input))
