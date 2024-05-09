#Binary Tree Traversal:
#If we want all 3 (Preorder , Inorder and Postorder Traversal in one code)
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:return 
        stack=[[root,1]]
        preorder=[]
        postorder=[]
        inorder=[]
        while stack:
            curr=stack.pop()
            if curr[1]==1:
                preorder.append(curr[0].val)
                curr[1]+=1
                stack.append(curr)
                if curr[0].left:
                    stack.append([curr[0].left,1])
            elif curr[1]==2:
                inorder.append(curr[0].val)
                curr[1]+=1
                stack.append(curr)
                if curr[0].right:
                    stack.append([curr[0].right,1])
            else:
                postorder.append(curr[0].val)
        return preorder

#We can also separate the code for individual traversals:

#PRE ORDER: 

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:return 
        stack=[[root,1]]
        preorder=[]
        while stack:
            curr=stack.pop()
            if curr[1]==1:
                preorder.append(curr[0].val)
                curr[1]+=1
                stack.append(curr)
                if curr[0].left:
                    stack.append([curr[0].left,1])
            elif curr[1]==2:
                curr[1]+=1
                stack.append(curr)
                if curr[0].right:
                    stack.append([curr[0].right,1])
        return preorder


#IN ORDER:

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:return 
        stack=[[root,1]]
        inorder=[]
        while stack:
            curr=stack.pop()
            if curr[1]==1:
                curr[1]+=1
                stack.append(curr)
                if curr[0].left:
                    stack.append([curr[0].left,1])
            elif curr[1]==2:
                inorder.append(curr[0].val)
                curr[1]+=1
                stack.append(curr)
                if curr[0].right:
                    stack.append([curr[0].right,1])
        return inorder


#POST ORDER: 

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:return 
        stack=[[root,1]]
        postorder=[]
        while stack:
            curr=stack.pop()
            if curr[1]==1:
                curr[1]+=1
                stack.append(curr)
                if curr[0].left:
                    stack.append([curr[0].left,1])
            elif curr[1]==2:
                curr[1]+=1
                stack.append(curr)
                if curr[0].right:
                    stack.append([curr[0].right,1])
            else:
                postorder.append(curr[0].val)
        return postorder
