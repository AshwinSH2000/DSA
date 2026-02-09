# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
key thing to remember: before you start processing any level, the elements in teh queue will be the level order traversal of that level. ashte.
to capture that you will use some methods. here we have used a value to count the length of queue before processing and pop exactly those many elements from the q.
'''
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = []
        level_size = 0
        result = []
        q.append(root)

        while q:
            level_size = len(q)
            level_nodes = []
            while (level_size>0):
                popped = q.pop(0)
                level_size -= 1
                level_nodes.append(popped.val)
                
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
            result.append(level_nodes)

        return result

            


        
        