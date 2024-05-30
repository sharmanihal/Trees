# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:  # If the tree is empty, it's symmetric
            return True
        ac
        # Use a helper function to perform DFS and check symmetry
        return self.dfs(root.left, root.right)
    
    def dfs(self, root1, root2):
        if not root1 or not root2:  # If either node is null, check if both are null
            return root1 == root2
        if root1.val != root2.val:  # If the values of nodes are different, it's not symmetric
            return False
        # Recursively check the symmetry of the left and right subtrees
        return self.dfs(root1.left, root2.right) and self.dfs(root1.right, root2.left)
     
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:  # If the tree is empty, it's symmetric
            return True
        
        # Helper function for DFS to check symmetry
        def dfs(root1, root2):
            if not root1 or not root2:  # If either node is null, check if both are null
                return root1 == root2
            if root1.val != root2.val:  # If the values of nodes are different, it's not symmetric
                return False
            # Check symmetry in left and right subtrees
            return dfs(root1.left, root2.right) and dfs(root1.right, root2.left)
        
        # Start DFS from the left and right children of the root
        return dfs(root.left, root.right)
     
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:  # If the tree is empty, it's symmetric
            return True
        
        if not root.left or not root.right:  # If either subtree is null, check if both are null
            return root.left == root.right
        
        # Use two queues to perform BFS and check symmetry
        queue1 = deque([root.left])
        queue2 = deque([root.right])
        
        while queue1 and queue2:  # While both queues are not empty
            node1 = queue1.popleft()  # Get the front node of the first queue
            node2 = queue2.popleft()  # Get the front node of the second queue
            
            if node1.val != node2.val:  # If the values of nodes are different, it's not symmetric
                return False
            
            # Check the right child of the first node with the left child of the second node
            if node1.right and node2.left:
                queue1.append(node1.right)
                queue2.append(node2.left)
            elif node1.right or node2.left:  # If only one of them is null, it's not symmetric
                return False
            
            # Check the left child of the first node with the right child of the second node
            if node1.left and node2.right:
                queue1.append(node1.left)
                queue2.append(node2.right)
            elif node1.left or node2.right:  # If only one of them is null, it's not symmetric
                return False
            
        return True
    
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:  # If the tree is empty, it's symmetric
            return True
        if not root.left or not root.right:  # If either subtree is null, check if both are null
            return root.left == root.right
        
        # Use a queue to perform BFS and check symmetry
        queue = deque([(root.left, root.right)])
        while queue:  # While the queue is not empty
            root1, root2 = queue.popleft()  # Get the front pair of nodes
            if not root1 and not root2:  # If both nodes are null, continue to the next pair
                continue
            if not root1 or not root2:  # If only one of them is null, it's not symmetric
                return False
            if root1.val != root2.val:  # If the values of nodes are different, it's not symmetric
                return False
            
            # Append the children of the current pair of nodes to the queue for further checking
            queue.append((root1.left, root2.right))
            queue.append((root1.right, root2.left))
        
        return True
