class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

p = Node(1)
p.left = Node(2)
p.right = Node(3)
q = Node(1)
q.left = Node(2)
q.right = Node(3)

class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not q or not p:
            return False
        if p.val != q.val:
                return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

z = Solution()
print (z.isSameTree(p,q))