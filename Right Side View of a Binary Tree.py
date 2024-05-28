class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        # Initialize a queue for BFS traversal
        queue = deque([(root, 0)])
        # A dictionary to store the rightmost node values at each level
        rightmost_nodes = defaultdict(int)
        
        while queue:
            level_size = len(queue)
            # Traverse nodes at the current level
            for _ in range(level_size):
                node, level = queue.popleft()
                # Update the rightmost node value for the current level
                rightmost_nodes[level] = node.val 
                # Add the child nodes to the queue
                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))
        
        # Return the values of the rightmost nodes in each level
        return [rightmost_nodes[i] for i in range(len(rightmost_nodes))]

    


class Solution:
    def __init__(self):
        self.rightmost_values = []
        
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        # Start the DFS traversal to get the rightmost values
        self.reversePreorder(root, 0)
        return self.rightmost_values
    
    def reversePreorder(self, root, level):
        if not root:
            return 
        
        # If the current level is not visited yet, add the rightmost value
        if len(self.rightmost_values) == level:
            self.rightmost_values.append(root.val)
        
        # Traverse right subtree first for getting rightmost values
        self.reversePreorder(root.right, level + 1)
        self.reversePreorder(root.left, level + 1)
        


class Solution:
    def __init__(self):
        self.rightmost_values = defaultdict(int)
        
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        # Start the DFS traversal to get the rightmost values
        self.reversePreorder(root, 0)
        # Return the values of rightmost nodes
        return self.rightmost_values.values()
    
    def reversePreorder(self, root, level):
        if not root:
            return 
        
        # If the current level is not visited yet, add the rightmost value
        if level not in self.rightmost_values:
            self.rightmost_values[level] = root.val
        
        # Traverse right subtree first for getting rightmost values
        self.reversePreorder(root.right, level + 1)
        self.reversePreorder(root.left, level + 1)

