class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def checkBST(root,low,high):
            if not root:
                return True
            if root.val<=low or root.val>=high:
                return False
            return checkBST(root.left,low,root.val) and checkBST(root.right,root.val,high)
        
        return checkBST(root,-math.inf,math.inf)
