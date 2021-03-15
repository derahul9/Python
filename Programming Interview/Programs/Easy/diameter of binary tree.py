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
    def diameterOfBinaryTree(self, root):
        if root is None:
            return 0
        lheight = self.height(root.left)
        rheight = self.height(root.right)

        ldiameter = self.diameterOfBinaryTree(root.left)
        rdiameter = self.diameterOfBinaryTree(root.right)
        return max(lheight + rheight, max(ldiameter, rdiameter))  #It could left height + right heigth or it could be completely on the left side or on the right side. So need to take max.

    def height(self, root):
        if root is None:
            return 0
        else:
            return 1 + max(self.height(root.left), self.height(root.right))

z = Solution()
print (z.diameterOfBinaryTree(root))