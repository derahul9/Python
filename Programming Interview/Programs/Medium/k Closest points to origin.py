points = [[3,3],[5,-1],[-2,4]]
K = 2

class Solution(object):
    def closePoints(self, points, K):
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:K]

z = Solution()
print (z.closePoints(points, K))
