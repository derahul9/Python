arr = [5, 1, 4, 3, 6, 8, 10, 7, 9]

# O(n) Solution
class Solution:
    def index(self, arr):
        n = len(arr)
        maximum_left = [None] * n
        maximum_left[0] = float('-inf')

        for i in range(1, n):
            maximum_left[i] = max(maximum_left[i - 1], arr[i - 1])
        print(maximum_left)
        print (arr)

        minimum_right = float('inf')

        for i in range(n - 1, -1, -1):
            if maximum_left[i] < arr[i] < minimum_right:
                return i

            minimum_right = min(minimum_right, arr[i])

        return -1

z = Solution()
print (z.index(arr))




