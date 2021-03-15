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
'''
Depth-First Search (DFS) Algorithms have three variants:
Inorder Traversal (left-current-right)— Visit the current node after visiting all nodes inside left subtree but before visiting any node within the right subtree.
Preorder Traversal (current-left-right)— Visit the current node before visiting any nodes inside left or right subtrees.
Postorder Traversal (left-right-current) — Visit the current node after visiting all the nodes of left and right subtrees.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
#Recursively (We can call our own function)
class Solution:
    def inorderTraversal(self, root):
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

z = Solution()
print (z.inorderTraversal(root))

#Iteratively (We can't call our own function)
class Solution1:
    def inorderTraversal1(self, root):
        stack = []
        result = []
        while root is not None or stack != []:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result

z = Solution1()
print (z.inorderTraversal1(root))

#Recursively (We can call our own function)
class Solution2:
    def preorderTraversal(self, root):
        if root is None:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

z = Solution2()
print (z.preorderTraversal(root))

#Iteratively (We can't call our own function)
class Solution3:
    def preorderTraversal1(self, root):
        if root is None:
            return []
        stack = [root]
        result = []
        while stack != []:
            root = stack.pop()
            result.append(root.val)
            if root.right is not None:
                stack.append(root.right)
            if root.left is not None:
                stack.append(root.left)
        return result

z = Solution3()
print (z.preorderTraversal1(root))

#Recursively (We can call our own function)
class Solution4:
    def postorderTraversal(self, root):
        if root is None:
            return []
        return  self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

z = Solution4()
print (z.postorderTraversal(root))

#Iteratively (We can't call our own function)
class Solution5:
    def postorderTraversal1(self, root):
        if root is None:
            return
        s1 = []
        s2 = []
        result = []
        s1.append(root)
        while s1:
            root = s1.pop()
            s2.append(root.val)
            if root.left:
                s1.append(root.left)
            if root.right:
                s1.append(root.right)
        while s2:
            root = s2.pop()
            result.append(root)
        return result

z = Solution5()
print (z.postorderTraversal1(root))

'''
------------------------------------------------------------------------------------------------------------------------
Breadth-First Search (BFS) Algorithm has one variant:
Level Order Traversal — Visit nodes level-by-level and left-to-right fashion at the same level.
------------------------------------------------------------------------------------------------------------------------
'''
#Iteratively (We can't call our own function)
class Solution6:
    def levelorderTraversal1(self, root):
        if root is None:
            return []
        queue = [root]
        next_queue = []
        level = []
        result = []
        while queue != []:
            for root in queue:
                level.append(root.val)
                if root.left is not None:
                    next_queue.append(root.left)
                if root.right is not None:
                    next_queue.append(root.right)
            result.append(level)
            level = []
            queue = next_queue
            next_queue = []
        return result

z = Solution6()
print (z.levelorderTraversal1(root))

