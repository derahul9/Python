nestedList = [[1,1],2,[1,1]]

class Solution:
    def nest(self, nestedList):
        def helper(nested, n):
            sum = 0
            for elements in nested:
                if type(elements) == int:
                    sum += n*elements
                if type(elements) == list:
                    sum += helper(elements, n+1)
            return sum

        return helper(nestedList, 1)

z = Solution()
print (z.nest(nestedList))


