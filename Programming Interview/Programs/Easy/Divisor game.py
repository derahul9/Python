n = 4

'''
Conclusion
If N is even, can win.
If N is odd, will lose.

Recursive Prove （Top-down)
If N is even.
We can choose x = 1.
The opponent will get N - 1, which is a odd.
Reduce to the case odd and he will lose.

If N is odd,
2.1 If N = 1, lose directly.
2.2 We have to choose an odd x.
The opponent will get N - x, which is a even.
Reduce to the case even and he will win.

So the N will change odd and even alternatively until N = 1.

Mathematical Induction Prove （Bottom-up)
N = 1, lose directly
N = 2, will win choosing x = 1.
N = 3, must lose choosing x = 1.
N = 4, will win choosing x = 1.
'''

class Solution:
    def Divisor(self, n):
        return n % 2 == 0

z = Solution()
print(z.Divisor(n))


class Solution1:
    def Divisor(self, n):
        def helper(n):
            for i in range(n-1, -1, -1):
                if n % i == 0:
                    return i
        while n > 1:
            alice = helper(n)
            n = n - alice
            if n == 1:
                return True
            else:
                bob = helper(n)
                n = n - bob
                if n == 1:
                    return False