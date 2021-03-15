A = [4,5,0,-2,-3,1]
K = 5

class Solution:
    def subarraysDivByK(self, A, K):
        a = 0
        sum = 0
        if len(A) == 1:
            if A[0] % K == 0:
                return 1
        for i in range(len(A)-1):
            sum = A[i]
            if A[i] % K == 0:
                a += 1
            for j in range(i+1, len(A)):
                sum += A[j]
                if sum % K == 0:
                    a += 1
        if A[len(A)-1] % K == 0:
            a += 1
        return a

z = Solution()
print (z.subarraysDivByK(A, K))