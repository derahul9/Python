n = 12

class Solution(object):
    def numSquares(self, n):
        square_nums = [i**2 for i in range(1, int((n**0.5))+1)]
        print (square_nums)

        def minNumSquares(k):
            """ recursive solution """
            # bottom cases: find a square number
            if k in square_nums:
                return 1
            min_num = float('inf')

            # Find the minimal value among all possible solutions
            for square in square_nums:
                if k < square:
                    break
                new_num = minNumSquares(k-square) + 1
                min_num = min(min_num, new_num)
                print (min_num)
            return min_num

        return minNumSquares(n)

z = Solution()
print (z.numSquares(n))