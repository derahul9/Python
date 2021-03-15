s = "226"

class Solution:
    def recursive_with_memo(self, index, s):
        if index == len(s):
            return 1
        if s[index] == '0':
            return 0
        if index == len(s)-1:
            return 1
        return self.recursive_with_memo(index+1, s) + (self.recursive_with_memo(index+2, s) if (int(s[index : index+2]) <= 26) else 0)

    def numDecodings(self, s):
        if not s:
            return 0
        return self.recursive_with_memo(0, s)

z = Solution()
print (z.numDecodings(s))
