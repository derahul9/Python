matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

class Solution:
    def rotate(self, matrix):
        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp
        return matrix

z = Solution()
print (z.rotate(matrix))