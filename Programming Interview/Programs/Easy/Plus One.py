digits = [1,2,3,4,9]
n = len(digits)
#print (range(n))

class Sum:
    def twoSum(self, digits):
        for i in range(n):
            last_element = n - 1 - i
            #print (digits[last_element])
            if digits[last_element] == 9:
                digits[last_element] = 0
            else:
                digits[last_element] = digits[last_element] + 1
                return digits

        return [1] + digits

z = Sum()
print (z.twoSum(digits))

