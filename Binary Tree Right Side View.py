# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:return []
        queue=deque([(root,0)])
        horizontalTable = defaultdict(int)
        while queue:
            size=len(queue)
            while size:
                node,level=queue.popleft()
                horizontalTable[level]=node.val 
                if node.left:
                    queue.append((node.left,level+1))
                if node.right:
                    queue.append((node.right,level+1))
                size-=1
        result=[]
        for i in range(0,len(horizontalTable)):
            result.append(horizontalTable[i])
        return result
            
            
