
class ListNode:
    def __init__ (self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def removeNode(self, node):
        while (node.next is not None):
            node.val = node.next.val
            if (node.next.next is None):
                node.next = None
            else:
                node = node.next

if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = None
    s = Solution()
    s.removeNode(node3)
    head = node1
    while head is not None:
        print(head.val)
        head = head.next
