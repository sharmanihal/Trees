# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#BFS Solution:
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue=deque()
		#Keep track of both parent and grandparent in the queue (for the root, it will be -1,1)
        queue.append([root,-1,-1])
        res=0
        while queue:
            size=len(queue)
            while size:
                node,parent,grandparent=queue.popleft()
				#If the grandparent of the node is even , add its value to the result
                if grandparent%2==0:
                    res+=node.val
                if node.left:
				#if node has a left, the current node will be it's parent and the parent of the current node will be its grandparent , so append the node accordingly
                    queue.append([node.left,node.val,parent])
                if node.right:
				#if node has a right, the current node will be it's parent and the parent of the current node will be its grandparent , so append the node accordingly
                    queue.append([node.right,node.val,parent])
                size-=1
        return res
		
#DFS Solution (Preorder)
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(root,parent,grandparent):
            nonlocal res
            if not root:
                return 0
            if grandparent%2==0:
                res+=root.val
			#if node has a left, the current node will be it's parent and the parent of the current node will be its grandparent , so append the node accordingly
            dfs(root.left,root.val,parent)
			#if node has a right, the current node will be it's parent and the parent of the current node will be its grandparent , so append the node accordingly
            dfs(root.right,root.val,parent)
        res=0
		#for the root, since it has no parent or grandparent , we pass -1 and -1
        dfs(root,-1,-1)
        return res
