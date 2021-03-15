s = "a)b(c)d"

class Solution:
    def valid(self, s):
        stack = []
        stack1 = []
        b =[]
        a = {i:v for i, v in enumerate(s)}
        print (a)
        for i, v in a.items():
            if v == "(":
                stack.append(i)
                stack1.append(v)
            if v == ")":
                if "(" in stack1:
                    stack.pop()
                    stack1.pop()
                else:
                    stack.append(i)
                    print (stack)
        for i in range(len(s)):
            if i not in stack:
                b.append(s[i])
        return "".join(b)

z = Solution()
print (z.valid(s))

