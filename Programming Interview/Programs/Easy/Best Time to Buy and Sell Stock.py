input = [7,1,5,3,6,4]

class Profit:
    def maxProfit(self, input):
        n = len(input)
        a = 0
        for i in range(n - 1, 0, -1):
            for j in range(i - 1, -1, -1):
                profit = input[i] - input [j]
                if profit > a:
                    a = profit
        return a

z = Profit()
print (z.maxProfit(input))