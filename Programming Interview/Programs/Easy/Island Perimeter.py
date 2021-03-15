grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

class Solution:
    def island(self, grid):
        per = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if i == 0 or grid[i-1][j] == 0:
                        per += 1
                    if i == (len(grid)- 1) or grid[i+1][j] == 0:
                        per += 1
                    if j == 0 or grid[i][j-1] == 0:
                        per += 1
                    if j == (len(grid[0])- 1) or grid[i][j+1] == 0:
                        per += 1
        return per

z = Solution()
print (z.island(grid))

