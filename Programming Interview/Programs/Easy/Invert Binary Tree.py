class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

root = Node(4)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(9)
'''
            4
        /       \
       2         7
    /     \   /    \
   1       3 6      9

'''

class Solution:
    def invertTree(self, root):
        if root is None:
            return []
        return self.invertTree(root.right) + [root.val] + self.invertTree(root.left)

z = Solution()
print (z.invertTree(root))