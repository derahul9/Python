dividend = 7
divisor = -3

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        i = 0
        if divisor >= 0 and dividend >= 0:
            while dividend >= divisor:
                dividend = dividend - divisor
                i += 1
            return i
        if divisor < 0 and dividend < 0:
            divisor = divisor * -1
            dividend = dividend * -1
            while dividend >= divisor:
                dividend = dividend - divisor
                i += 1
            return i
        if divisor < 0:
            divisor = divisor * -1
            while dividend >= divisor:
                dividend = dividend - divisor
                i += 1
            return i * -1
        if dividend < 0:
            dividend = dividend * -1
            while dividend >= divisor:
                dividend = dividend - divisor
                i += 1
            return i * -1

z = Solution()
print (z.divide(dividend, divisor))