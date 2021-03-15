S = "abbaca"

class Solution:
    def removeDuplicates(self, S):
        output = []
        for ch in S:
            if output and ch == output[-1]:
                output.pop()
            else:
                output.append(ch)
        return ''.join(output)

z = Solution()
print (z.removeDuplicates(S))