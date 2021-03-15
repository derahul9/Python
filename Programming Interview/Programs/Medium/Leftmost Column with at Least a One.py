mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
mat1 = [[0,0],[0,0]]

class Solution:
    def left(self, mat):
        for i in range(len(mat[0])):
            for j in range ((len(mat))):
                if mat[i][j] == 1:
                    return i
        return -1

z = Solution()
print (z.left(mat1))