# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
i feel this is normal bfs travel but a slight tweak to alter the order of
'''
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append(root)
        result = []
        reverse = False
        while q:
            level_nodes_count = len(q)
            level_nodes = []
            while level_nodes_count > 0:
                node = q.popleft() #gets th first element from the queue
                level_nodes.append(node.val)
                level_nodes_count -= 1

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            if reverse:
                result.append(level_nodes[::-1])
                reverse = False
            else:
                result.append(level_nodes)
                reverse = True

        return result