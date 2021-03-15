workers = [[0,0],[2,1]]
bikes = [[1,2],[3,3]]

class Solution:
    def campus(self, workers, bikes):
        a = []
        b= []
        for i in range(len(workers)):
            for j in range(len(bikes)):
                dist = abs(bikes[j][0] - workers[i][0]) + abs(bikes[j][1] - workers[i][1])
                a.append([dist, i, j])
        y = sorted(a, key=lambda P: P[0])
        res = [-1] * len(workers)                                        #The part from here is really difficult to imagine with the [-1]* len(workers) thing.
        used = []                                                        #Run it line by line
        for dist, worker, bike in y:
            if res[worker] == -1 and bike not in used:
                res[worker] = bike
                used.append(bike)
        return res

z = Solution()
print (z.campus(workers, bikes))