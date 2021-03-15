input = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4

class Solution:
    def freq(self, input, k):
        input.sort(key = lambda I: input.count(I[0]), reverse =1)
        return input[:k]

z = Solution()
print (z.freq(input, k))
