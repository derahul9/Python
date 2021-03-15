gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

class Solution:
    def gasS(self, gas, cost):
        n = len(gas)
        total_tank, curr_tank = 0, 0
        starting_station = 0
        for i in range(n):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            if curr_tank < 0:
                starting_station = i + 1
                curr_tank = 0
        return starting_station if total_tank >= 0 else -1

z = Solution()
print (z.gasS(gas, cost))
