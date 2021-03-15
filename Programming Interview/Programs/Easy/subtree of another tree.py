class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

s = Node(3)
s.left = Node(4)
s.right = Node(5)
s.left.left = Node(1)
s.left.right = Node(2)

t = Node(4)
t.left = Node(1)
t.right = Node(2)


class Solution:
    def isSubtree(self, s, t):
        if not t: return True
        if not s: return False
        if self.isSametree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSametree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return False
        return self.isSametree(s.left, t.left) & self.isSametree(s.right, t.right)

z = Solution()
print (z.isSubtree(s, t))