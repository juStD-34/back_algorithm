class ListNode:
    def __init__ (self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        if head == None or head.next == None:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p

if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    s = Solution()
    head = s.reverseList(node1)
    while head is not None:
        print(head.val)
        head = head.next