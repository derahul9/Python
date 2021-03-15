class Node:
    def __init__(self,key):
        self.next = None
        self.val = key

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

class Solution(object):
    def LLPrint(self, prev):
        while prev:
            print (prev.val)
            prev = prev.next

    def reverseList(self, head):  # Iterative
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return self.LLPrint(prev)

z = Solution()
print (z.reverseList(head))