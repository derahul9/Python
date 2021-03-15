input = [23, 2, 8, 7, 4, 6, 8, 7]
k=15

class Continuous:
    def contSub(self, input, k):
        n = len(input)
        for i in range(n):
            x = input[i]
            for j in range(i +1, n):
                x +=  input[j]
                print (x)
                if x % k == 0:
                    return True
        return False

z = Continuous()
print (z.contSub(input, k))