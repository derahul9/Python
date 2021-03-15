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

class Solution6:
    def levelorderTraversal1(self, root):
        if root is None:
            return []
        s1 = [root]
        s2 = []
        level = []
        result = []
        while s1 or s2:
            while s1:
                root = s1.pop()
                level.append(root.val)
                if root.left is not None:
                    s2.append(root.left)
                if root.right is not None:
                    s2.append(root.right)
            result.append(level)
            level = []
            while s2:
                root = s2.pop()
                level.append(root.val)
                if root.right is not None:
                    s1.append(root.right)
                if root.left is not None:
                    s1.append(root.left)
            if level != []:
                result.append(level)
                level = []
        return result

z = Solution6()
print (z.levelorderTraversal1(root))