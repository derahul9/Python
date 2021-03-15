n = 10

class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0
        if n == 3:
            return 1
        if n >= 3:
            cou =2
        for i in range(2, n):
            for j in range(2, i):
                if i % j == 0 and i != j:
                    break
                if i % j != 0:
                    if j == i // 2:
                        print (i)
                        cou += 1
        return cou

z = Solution()
print (z.countPrimes(n))