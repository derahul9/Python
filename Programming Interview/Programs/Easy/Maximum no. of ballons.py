text = "balloonballoonballoonballoon"

class Solution:
    def maxNumberOfBalloons(self, text):
        m = float('inf')
        from collections import defaultdict
        a = defaultdict(int)
        b = defaultdict(int)
        for elem in "balloon":
            a[elem] = "balloon".count(elem)
        for data in text:
            b[data] = text.count(data)
        for i, v in a.items():
            if i not in b:
                return 0
            if i in b:
                x = b[i] // a[i]
                m = min(x, m)
        return m

z = Solution()
print (z.maxNumberOfBalloons(text))