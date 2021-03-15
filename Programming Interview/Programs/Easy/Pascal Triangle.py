num_rows = 5

class Solution:
    def generate(self, num_rows):
        triangle = []

        for row_num in range(num_rows):

            # The first and last row elements are always 1.
            row = [None for i in range(row_num+1)]
            print (row)
            row[0], row[-1] = 1, 1
            print(row)

            for j in range(1, len(row) - 1):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
            triangle.append(row)
        return triangle

z = Solution()
print (z.generate(num_rows))
