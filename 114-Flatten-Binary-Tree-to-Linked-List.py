# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        
        [2:00]: I observe that a dfs traversal is done and
        returned as a linked list
        
        Brute Force solution would be to do a DFS traversal,
        store it in a list
        connect each lists right node to each other.
        However, it's not inplace, O(n) runtime, O(n) space
        
        Ideally, it's better to do this in constant space
        [5:00]: Code brute force
        [7:30]: Ran code to verify
        [11:30]: Implemented brute force
        
        Edge cases
        [] -> []
        [1] -> [1]
        [13:30]: Brute force passed all test cases
        
        [14:46]: Looked at hint
        Using pre-order traversal, point each node's right child to next node
        #preorder
        node.left
        node
        node.right
        [28:00] Partly understood Moris traversal algo. Wasn't able to implement it
        
        """
        if not root:
            return None

        dfs_order = []
        st = [root]
        visited = set()
        #dfs
        while(st):
            curr = st.pop()
            if curr not in visited:
                visited.add(curr)
                dfs_order.append(curr)
                
            if curr.right:
                st.append(curr.right)    
                
            if curr.left:
                st.append(curr.left)
                
        if len(dfs_order) == 1:
            return root
            
        root = dfs_order[0]
        for i, node in enumerate(dfs_order):
            node.left = None
            if i != 0:
                dfs_order[i - 1].right = node
      
