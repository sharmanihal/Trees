class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root,freq):
            if not root:
                return 0
            left_sum = dfs(root.left,freq)
            right_sum = dfs(root.right,freq)
            total_sum=left_sum + right_sum + root.val
            freq[total_sum] = freq.get(total_sum,0) + 1
            return total_sum
        
        freq=defaultdict()
        dfs(root,freq)
        
        #Find element with max freq
        max_freq = max(freq.values())
        #Create the resultant array with all element that have the max_freq
        res=[]
        for i in freq:
            if freq[i] == max_freq:
                res.append(i)
        return res
