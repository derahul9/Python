input = [[0,30],[5,10],[15,20]]

class Solution:
    def meet(self, input):
        if input == []:
            return 0
        a = []
        b = []
        x = sorted(input, key=lambda P: P[0])
        for elements in x:
            a.append(elements[0])
        y = sorted(input, key=lambda P: P[1])
        for elements in y:
            b.append(elements[1])
        print (a)
        print (b)
        i = 0
        j = 0
        k = 0
        while j < len(a):
            if a[j] >= b[k]:
                i -=1
                k +=1
            j += 1
            i +=1
        return i

z = Solution()
print (z.meet(input))