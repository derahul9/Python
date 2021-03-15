Input = [0,1,0,3,12]
Input1 = [0,0,0,0,1]

class Zero:
    def moveZeroes(self, Input):
        for elements in Input:
            if elements == 0:
                Input.remove(0)
                Input.append(0)
        return Input

z = Zero()
print (z.moveZeroes(Input))
