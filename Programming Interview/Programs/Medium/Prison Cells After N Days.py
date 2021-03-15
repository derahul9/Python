cells = [0,1,0,1,1,0,0,1]
N = 7

class Prison:
    def prisonCells(self, cells, N):
        cells1 = []
        for i in range(N):
            l = len(cells)
            for j in range(1,l-1):
                if int(cells[j-1]) + int(cells[j+1]) == 0 or int(cells[j-1]) + int(cells[j+1]) == 2:
                    cells1.insert(j, 1)
                else:
                    cells1.insert(j, 0)
            cells1.insert(0, 0)
            cells1.insert(l-1, 0)
            cells = cells1
            cells1 = []
        return cells

z = Prison()
print (z.prisonCells(cells, N))




