s = "(]"
s1 = "()[]{}"

class Valid():
    def isValid(self, s):
        left = ['(', '{', '[']
        right = [')', '}', ']']
        stack = []
        for letter in s:
            if letter in left:
                stack.append(letter)
            elif letter in right:
                if left.index(stack.pop()) != right.index(letter):
                    return False
        return len(stack) == 0

z = Valid()
print (z.isValid(s1))