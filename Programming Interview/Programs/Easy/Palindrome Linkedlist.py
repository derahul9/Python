class Node:
    def __init__(self,key):
        self.next = None
        self.val = key

head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(1)

class Solution(object):
    def reverseList(self, head):  # Iterative
        a = []
        curr = head
        while curr is not None:
            a.append(curr.val)
            curr = curr.next
        return a == a[::-1]

z = Solution()
print (z.reverseList(head))