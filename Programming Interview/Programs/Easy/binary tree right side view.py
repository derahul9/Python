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
'''
            1
        /       \
       2         3
    /     \   /    \
   4       5 6      7

'''

class Solution:
    def rightSideView(self, root):
        if root is None:
            return []
        return [root.val] + self.rightSideView(root.right)

z = Solution()
print (z.rightSideView(root))