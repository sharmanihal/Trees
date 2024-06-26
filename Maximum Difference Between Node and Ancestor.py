# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(root,minValue,maxValue):
            nonlocal res
            if not root:return
            #Keep track of the min value seen till now, if root value if lower ,replace the min value with it
            minValue=min(root.val,minValue)
            #Keep track of the max value seen till now, if root value if higher ,replace the max value with it
            maxValue=max(root.val,maxValue)
            #Since we will have min and max value seen till now, check if the already existing result is higher or
            #1. Absolute of root value minus the min value is higher than result, if yes update the result
            #2. Absolute of root value minus the max value is higher than result, if yes update the result
            res=max(res,abs(root.val-minValue),abs(root.val-maxValue))
            #Check the left side sub tree, with the min and max value
            dfs(root.left,minValue,maxValue)
            #Check the right side sub tree, with the min and max value
            dfs(root.right,minValue,maxValue)
        res=0
        dfs(root,root.val,root.val)
        return res
