strs = ["flower","flow","flight"]

class Solution:
    def longestCommonPrefix(self, strs):
        a = []
        str = sorted(strs, key = lambda P:len(P))
        result = ''
        for i in range(1, len(str[0])+1):
            prefix = str[0][:i]
            for words in str:
                if words[:i] != prefix:
                    return result
            result = prefix
        return result

z = Solution()
print (z.longestCommonPrefix(strs))
