class ListNode:
    def __init__ (self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        if (head is None):
            return head
        if (head.next is None):
            return None
        current = head
        length = 0
        while(current.next is not None):
            current = current.next
            length += 1
        removeIndex = length - n + 1
        if (removeIndex == 0):
            return head.next
        index = 0 
        current = head
        while (index < removeIndex - 1):
            current = current.next
            index += 1
        current.next = current.next.next
        return head

if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    # node2.next = node3
    # node3.next = node4
    s = Solution()
    s.removeNthFromEnd(node1, 2)
    head = node1
    while head is not None:
        print(head.val)
        head = head.next