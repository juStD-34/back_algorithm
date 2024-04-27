class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        prev = None
        while head is not None:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev
            
    def isPalindrome(self, head):
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        print(slow.val)
        if fast is not None:
            slow = slow.next
        slow = self.reverseList(slow)
        fast = head
        
        while slow is not None:
            print(slow.val, fast.val)
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next
        return True

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(5)
    node4 = ListNode(2)
    node5 = ListNode(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    s = Solution()
    print(s.isPalindrome(node1))
    # while head is not None:
    #     print(head.val)
    #     head = head.next
    