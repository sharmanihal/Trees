class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(root,is_left,length):
            if not root:
                return
            nonlocal res
            res=max(res,length)
            #If the previous move was left, for zig zag to continue we need to take a right (if any)
            if is_left:
                dfs(root.right,False,length+1)
                #If no right node, means we'll have to reset the zig zag length and start from left node
                dfs(root.left,True,1)
            #If the previous move was right, for zig zag to continue we need to take a left (if any)
            else:
                dfs(root.left,True,length+1)
                #If no left node, means we'll have to reset the zig zag length and start from right node
                dfs(root.right,False,1)
        res=0
        dfs(root,True,0)
        dfs(root,False,0)
        return res
                    
