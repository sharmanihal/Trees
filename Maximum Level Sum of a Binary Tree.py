class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        #Initially the result level and max sum is 1 and root.val respectively
        level, res = 1, 1
        max_sum = root.val
        queue = deque([root])
        
        #BFS for each level
        while queue:
            current_sum = 0
            #For each level:
            for _ in range(len(queue)):
                node = queue.popleft()
                current_sum += node.val  # Add node's value to current level's sum
                if node.left:
                    queue.append(node.left)  # Add left child to the queue
                if node.right:
                    queue.append(node.right)  # Add right child to the queue
            
            # Update result level if current level's sum is greater than max_sum
            if current_sum > max_sum:
                max_sum = current_sum
                res = level
            
            level += 1  # Move to the next level
        
        return res
    
    
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node, level):
            if not node:
                return
            level_map[level] = level_map.get(level, 0) + node.val
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        # Hashmap to store the sum of values at each level
        level_map = {}
        dfs(root, 1)
        
        # Find the level with the maximum sum
        max_sum = root.val
        min_level = 1
        for level in level_map:
            if level_map[level] > max_sum :
                max_sum = level_map[level]
                min_level = level
                
        return min_level
        
