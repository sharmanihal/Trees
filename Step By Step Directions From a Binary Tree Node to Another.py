class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        if not root:
            return
        
        def lca(root, p, q):
            if not root or root.val == p or root.val == q:
                return root
            left = lca(root.left, p, q) 
            right = lca(root.right, p, q)
            if left and right:
                return root
            return left if left else right
        
        # Finding the Lowest Common Ancestor (LCA) of startValue and destValue
        lowestCommanAncestor = lca(root, startValue, destValue)
        
        # Function to get directions from LCA to a specific value
        def getDirection(root, value, array):
            if not root:
                return None
            if root.val == value:
                return array
            array.append("L")  # Assume left direction
            left = getDirection(root.left, value, array)
            if not left:
                array.pop()  # If no path found on left, backtrack
                array.append("R")  # Assume right direction
                right = getDirection(root.right, value, array)
                if not right:
                    array.pop()  # If no path found on right, backtrack
            return left if left else right
        
        # Get directions from LCA to startValue
        start = getDirection(lowestCommanAncestor, startValue, [])
        
        # Get directions from LCA to destValue
        end = getDirection(lowestCommanAncestor, destValue, [])
        
        # Concatenate "U" (up) for the length of start directions
        return "U" * len(start) + "".join(end)
