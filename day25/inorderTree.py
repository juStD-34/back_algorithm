class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root):
        """return type: List[int]"""
        def helper(root,result):
          if root != None:
            helper(root.left,result)
            result.append(root.val)
            helper(root.right,result)  
            
        result = []
        helper(root,result)
        return result
            