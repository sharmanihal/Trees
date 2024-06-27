class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(root,target):
            if not root:
                return None
            left= dfs(root.left,target)
            if not left:root.left=None
            right=dfs(root.right,target)
            if not right:root.right=None
            #If its a leaf node and value is equal to target, we need to delete it.
            if not left and not right and root.val==target:
                return None
            return root.val
        dfs(root,target)
        if not root.left and not root.right and root.val==target:return None
        return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def dfs(root,target,parent):
            if not root:
                return None
            left= dfs(root.left, target,parent)
            right=dfs(root.right,target,parent)
            #If its a leaf node and value is equal to target, we need to delete it.
            if not left and not right and root.val==target:
                #Use parent hashmap to find parent of the this leaf node and set that to none
                if root in parent:
                    parent_node=parent[root]
                    if parent_node.left==root:
                        parent_node.left=None
                    if parent_node.right==root:
                        parent_node.right=None
                return None
            return root.val

        def bfs_to_find_parent(root):
            parent={}
            if not root:
                return parent
            queue=deque()
            queue.append(root)
            while queue:
                node=queue.popleft()
                if node.left:
                    queue.append(node.left)
                    parent[node.left]=node
                if node.right:
                    queue.append(node.right)
                    parent[node.right]=node
            return parent
        parent=bfs_to_find_parent(root)
        dfs(root,target,parent)
        if not root.left and not root.right and root.val==target:return None
        return root
    
    
