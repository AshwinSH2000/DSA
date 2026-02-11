"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

'''
simple approach as the binary level order traversal. 
only thing to keep in mind is to check if the children exist and if they do, push them into the queue
'''
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append(root)
        result = []
        while q:
            level_nodes = []
            level_nodes_len = len(q)
            while level_nodes_len > 0:
                node = q.popleft()
                level_nodes.append(node.val)
                level_nodes_len -= 1

                if node.children:
                    for child in node.children:
                        q.append(child)

            result.append(level_nodes)

        return result
        