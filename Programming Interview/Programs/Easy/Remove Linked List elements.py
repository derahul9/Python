class Node:
    def __init__(self,key):
        self.next = None
        self.val = key

head = Node(1)
head.next = Node(2)
head.next.next = Node(6)
head.next.next.next = Node(3)
head.next.next.next.next = Node(4)
head.next.next.next.next.next = Node(5)
head.next.next.next.next.next.next = Node(6)

input = 6

class Solution(object):
    def LLPrint(self, curr):
        while curr:
            print (curr.val)
            curr = curr.next

    def removeList(self, head, input):  # Iterative
        prev = None
        curr = head
        while curr:
            if curr.val == input:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        curr = head
        return self.LLPrint(curr)

z = Solution()
print (z.removeList(head, input))