class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []  # If the root is None, return an empty list
        
        zigzag = []  # List to store the zigzag traversal
        queue = deque()  # Queue for level-order traversal
        queue.append(root)  # Add the root node to the queue
        left_to_right = True  # Boolean flag to indicate direction
        
        while queue:
            level_size = len(queue)  # Get the number of nodes at the current level
            level_nodes = []  # List to store nodes at the current level
            
            # Traverse each node at the current level
            for _ in range(level_size):
                curr_node = queue.popleft()  # Remove the node from the left side of the queue
                if left_to_right:
                    level_nodes.append(curr_node.val)  # Append node value if left to right
                else:
                    level_nodes.insert(0, curr_node.val)  # Insert node value at the beginning if right to left
                
                # Add left and right child nodes to the queue if they exist
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            
            zigzag.append(level_nodes)  # Add nodes at the current level to the result list
            left_to_right = not left_to_right  # Toggle the direction for the next level
        
        return zigzag
