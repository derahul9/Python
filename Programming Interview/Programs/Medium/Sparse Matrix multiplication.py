a = [[ 1, 0, 0], [-1, 0, 3]]
b = [[ 7, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 1 ]]

class Solution:
    def matmul(self, a, b):
        x = []
        y = []
        sum = 0
        for c in range(len(a)):
            for d in range(len(b[0])):
                for e in range(len(b)):
                    sum += a[c][e]*b[e][d]
                x.append(sum)
                sum = 0
            y.append(x)
            x = []
        return y

z = Solution()
print (z.matmul(a, b))
