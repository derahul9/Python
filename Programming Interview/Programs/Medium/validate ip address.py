IP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
IP1 = "23.23.231.23"

class Solution:
    def valid(self, IP):
        ans = []
        if len(IP.split(".")) == 4:
            ans = IP.split(".")
            for data in ans:
                for data1 in data:
                    if data1 not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                        return "Neither"
            for elements in ans:
                if int(elements) > 255 or int(elements) < 0:
                    return "Neither"
                if len(elements.lstrip("0")) != len(elements):
                    return "Neither"
            return "IPv4"
        if len(IP.split(":")) == 8:
            ans = IP.split(":")
            for elements in ans:
                if len(elements) > 4 or len(elements) < 1:
                    return "Neither"
                for data in elements:
                    if data not in ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","A","B","C","D","E","F"]:
                        return "Neither"
            return "IPv6"
        return "Neither"

z = Solution()
print (z.valid(IP1))
