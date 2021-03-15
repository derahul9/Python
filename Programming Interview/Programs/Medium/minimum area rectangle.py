input = [[1,1],[3,3],[1,3],[3,1],[2,2]]

class Solution:
    def minAreaRect(self, input):
        area = 0
        ans = float('inf')
        for i in range(len(input)):
            for j in range(len(input)):
                if i != j:
                    if (input[i][0] != input[j][0] and input[i][1] != input[j][1] and [input[j][0],input[i][1]] in input and [input[i][0],input[j][1]] in input):
                        area = abs(input[i][1]-input[j][1])*abs(input[i][0]-input[j][0])
                        ans = min(area, ans)
        if ans == float('inf'):
            return 0
        else:
            return ans

z = Solution()
print (z.minAreaRect(input))
