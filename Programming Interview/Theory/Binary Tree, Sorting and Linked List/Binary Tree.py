#Creating and Inserting into a tree
#Binary Tree - Properties
#1. The maximum number of nodes at level ‘l’ of a binary tree is 2^l.
#2. The maximum number of nodes in a binary tree of height h is 2^h -1.
#3. In a Binary Tree with N nodes, minimum possible height or the minimum number of levels is Log2(N+1).
#4. Full Binary Tree - A Binary Tree is a full binary tree if every node has 0 or 2 children.
#We can also say a full binary tree is a binary tree in which all nodes except leaf nodes have two children.
#5. Complete Binary Tree: A Binary Tree is a complete Binary Tree if all the levels are completely filled except possibly the last level and the last level
# has all keys as left as possible
#6. Perfect Binary Tree A Binary tree is a Perfect Binary Tree in which all the internal nodes have two children and all leaf nodes are at the same level.

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+" Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+" Not Found"
            return self.right.findval(lkpval)
        else:
            print(str(self.data) + ' is found')

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.PrintTree()
print(root.findval(7))
print(root.findval(14))