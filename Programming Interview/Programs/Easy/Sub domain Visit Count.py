i = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]

class Solution:
    def visit(self, i):
        from collections import defaultdict
        b = []
        a = defaultdict(int)
        for elements in i:
            spa = elements.split(" ")
            a[spa[1]] += int(spa[0])
            do = spa[1].split(".")
            if len(do) == 3:
                a[do[2]]  += int(spa[0])
                a[do[1] + "." + do[2]] += int(spa[0])
            if len(do) == 2:
                a[do[1]]  += int(spa[0])
        for dom, ct in a.items():
            b.append("{} {}".format(ct, dom))
        return b

z = Solution()
print (z.visit(i))