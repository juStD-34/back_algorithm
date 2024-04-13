class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(self, list1, list2):
    ans =ListNode()
    count = 0
    while (list1 is not None and list2 is not None):
        if list1.val < list2.val:
            ans.val = list1.val
            list1 = list1.next
        elif list1.val >= list2.val:
            ans.val = list2.val
            list2 = list2.next
        elif (list1 is None):
            ans.val = list2.val
            list2 = list2.next
        else:
            ans.val = list1.val
            list1 = list1.next
        newNode = ListNode()
        ans.next = newNode

    return ans

node1 = ListNode(1)
node2 = ListNode(3)
node3 = ListNode(4)
node1.next = node2
node2.next = node3

node4 = ListNode(1)
node5 = ListNode(2)
node6 = ListNode(4)
node4.next = node5
node5.next = node6

if __name__ == "__main__":
    print(mergeTwoLists(0, node1, node4))
    