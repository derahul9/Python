class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(5)
root.right.right = Node(4)
'''
            1
        /       \
       2         2
    /     \   /    \
   4       5 5      4
'''

class Solution(object):
    def symTree(self, root):
        def isSym(root1, root2):
            if root1 == None and root2 == None:
                return True
            elif root1 == None and root2 != None:
                return False
            elif root1 != None and root2 == None:
                return False
            else:
                if root1.val != root2.val:
                    return False
                else:
                    return isSym(root1.left, root2.right) and isSym(root1.right,root2.left)
        return root == False or isSym(root.left,root.right)

z = Solution()
print (z.symTree(root))
