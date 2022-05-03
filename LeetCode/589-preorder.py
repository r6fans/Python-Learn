"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# 递归
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        def dfs(node: 'Node'):
            if node == None:
                return
            ans.append(node.val)
            if node.children != None:
                for ch in node.children:
                    dfs(ch)
        dfs(root)
        return ans