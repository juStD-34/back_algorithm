from day25.inorderTree import Solution

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def helper(self, p, q):
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val == q.val:
            return self.helper(p.left, q.left) and self.helper(p.right, q.right)
        else:
            return False
    def isSameTree(self, p, q):
        while p != None or q != None:
            if self.helper(p, q):
                return True
            else:
                return False
        return True