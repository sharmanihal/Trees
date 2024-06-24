    def averageOfSubtree(self, root: TreeNode) -> int:
        def dfs(root):
            nonlocal res
            if not root:
                return 0,0
            left,nodesInLeft=dfs(root.left)
            right,nodesInRight=dfs(root.right)
            if (root.val+left+right)//(nodesInLeft+nodesInRight+1)==root.val:
                res+=1
            return root.val+left+right,nodesInLeft+nodesInRight+1
        res=0
        dfs(root)
        return res
