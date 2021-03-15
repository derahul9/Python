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

class Solution(object):
    def depthOfBinaryTree(self, root):
        if not root:
            return 0
        ans = 1 + max(self.depthOfBinaryTree(root.left), self.depthOfBinaryTree(root.right))
        return ans

z = Solution()
print (z.depthOfBinaryTree(root))