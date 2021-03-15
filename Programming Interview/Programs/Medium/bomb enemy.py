inp = [["0","E","0","0"],
      ["E","0","W","E"],
      ["0","E","0","0"]]

class Solution:
    def bomb(self, inp):
        if len(inp) == 0:
            return 0
        rows, cols = len(inp), len(inp[0])

        def killEnemies(row, col):
            enemy_count = 0
            row_ranges = [range(i - 1, -1, -1), range(i + 1, rows, 1)]
            for row_range in row_ranges:
                for r in row_range:
                    if inp[r][col] == 'W':
                        break
                    elif inp[r][j] == 'E':
                        enemy_count += 1

            col_ranges = [range(j - 1, -1, -1), range(j + 1, cols, 1)]
            for col_range in col_ranges:
                for c in col_range:
                    if inp[i][c] == 'W':
                        break
                    elif inp[i][c] == 'E':
                        enemy_count += 1

            return enemy_count

        max_count = 0
        for i in range(rows):
            for j in range(cols):
                if inp[i][j] == "0":
                    max_count = max(max_count, killEnemies(i, j))
        return max_count

z = Solution()
print (z.bomb(inp))



