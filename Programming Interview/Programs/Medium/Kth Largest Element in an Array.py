input = [3,2,3,1,2,4,5,5,6]
k = 4

input1 = [3,2,1,5,6,4]
k1 = 2

class Solution():
    def kLargest(self, input, k):
        input.sort(reverse=1)                              #This function will change the list itself you can't store this in a variable. To store use sorted function
        return (input[(k -1)])

class Solution1():
    def kLargest(self, input1, k1):
        input2 = sorted(input1)
        return (input2[len(input2) -k1])

z = Solution()
print (z.kLargest(input, k))

r = Solution1()
print (r.kLargest(input1, k1))







