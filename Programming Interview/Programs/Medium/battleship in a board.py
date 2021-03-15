arr = [["X", ".", ".", "X"],
       [".", "X", "X", "."],
       [".", ".", ".", "X"]]

class Solution:
    def battle(self, arr):
        row = len(arr)
        col = len(arr[0])
        count  = 0
        for i in range(row):
            for j in range(col):
                if arr[i][j] == "X" and (i == 0 or arr[i-1][j] == ".") and (j == 0 or arr[i][j-1] == "."):
                    count +=1
        return count

z = Solution()
print (z.battle(arr))


#This solution works due to two reasons:
#Battleships are not contagious to each other
#Battleships are shaped as 1n or n1 rectangles