intervals = [[1,3],[2,6],[8,10],[15,18]]

class Solution:
    def merge(self, intervals):
        a = []
        intervals.sort(key = lambda P: P[0])
        for data in intervals:
            if not a or a[-1][1] < data[0]:
                a.append(data)
            else:
                a[-1][1] = max(data[1], a[-1][1])

        return a

z = Solution()
print (z.merge(intervals))