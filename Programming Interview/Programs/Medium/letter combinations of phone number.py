digits = "23"

phone = {'2': ['a', 'b', 'c'],
         '3': ['d', 'e', 'f'],
         '4': ['g', 'h', 'i'],
         '5': ['j', 'k', 'l'],
         '6': ['m', 'n', 'o'],
         '7': ['p', 'q', 'r', 's'],
         '8': ['t', 'u', 'v'],
         '9': ['w', 'x', 'y', 'z']}

# Very good example for a recursive function
# Combination - Order doesn't matter (so number of comb will be less)
# Permutation - Order matters (So each arrangement considering all the possible order will make up permutation and hence more in number)

class Solution:
    def combo(self, digits, phone):
        def backtrack(combination, next_digits):
            if len(next_digits) == 0:
                output.append(combination)
            else:
                for letter in phone[next_digits[0]]:
                    backtrack(combination + letter, next_digits[1:])

        output = []
        if digits:
            backtrack("", digits)
        return output

z = Solution()
print (z.combo(digits, phone))


class Solution1:
    def combo1(self, digits, phone):
        from itertools import combinations
        return combinations(phone[digits[0]]+phone(digits[1]), 2)

z = Solution1()
print (z.combo1(digits, phone))