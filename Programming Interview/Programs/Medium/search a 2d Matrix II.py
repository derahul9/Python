matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 1

class Matrix:
    def searchMatrix(self, matrix, target):
        o = -1
        for elements in matrix:
            l = len(elements)
            n = l // 2
            o = o + 1
            if target > elements[n]:
                for j in range(n+ 1, l):
                    if target == elements[j]:
                        print ("1")
                        return (o, j)
            if target < elements[n]:
                for k in range(0, n):
                    if target == elements[k]:
                        print ("2")
                        return (o, k)
            if target == elements[n]:
                print ("3")
                return (o, n)
        return False

z = Matrix()
print (z.searchMatrix(matrix, target))