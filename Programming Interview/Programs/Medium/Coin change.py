coins = [186,419,83,408]
amount = 6249

class Solution:
    def coin(self, coins, amount):
        coins.sort(reverse=True)
        print (coins)
        n = 0
        count = 0
        while n < len(coins):
            x = amount // coins[n]
            if x == 0:
                n += 1
                print (x)
            else:
                print (x)
                count += x
                amount = amount % coins[n]
                print (amount)
                n += 1
        if amount == 0:
            return count
        else:
            return -1


z = Solution()
print (z.coin(coins, amount))
