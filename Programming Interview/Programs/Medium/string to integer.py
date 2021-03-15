str = "-91283472332"

class Solution:
    def myAtoi(self, s: str) -> int:
        x = ["-", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        a = s.lstrip(" ")
        b = a.split(" ")[0]
        if b[0] not in x:
            return 0
        elif -2147483647 > int(b):
            return -2147483648
        elif int(b) > 2147483647:
            return 2147483648
        else:
            return int(b)

z = Solution()
print (z.myAtoi(str))

