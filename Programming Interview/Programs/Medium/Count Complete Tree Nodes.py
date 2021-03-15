class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

class Solution:
    def countNodes(self, root):
        if root is not None:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        else:
            return 0

z = Solution()
print (z.countNodes(root))