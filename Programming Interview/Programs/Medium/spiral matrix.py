arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

class Solution:
    def spiral(self, arr):
        a = []
        r = len(arr)
        c = len(arr[0])
        T = 0
        L = 0
        B = r - 1
        R = c - 1
        dir = 0
        while T < B or L < R:
            if dir == 0:
                for i in range(L, R+1):
                    a.append(arr[T][i])
                T += 1
            if dir == 1:
                for i in range(T, B+1):
                    a.append(arr[i][R])
                R -= 1
            if dir == 2:
                for i in range(R, L-1, -1):
                    a.append(arr[B][i])
                B -= 1
            if dir == 3:
                for i in range(B, T-1, -1):
                    a.append(arr[i][L])
                L += 1
            dir = (dir + 1) % 4
        return a

z = Solution()
print (z.spiral(arr))
