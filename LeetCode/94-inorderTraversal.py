# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def Travel(subroot: Optional[TreeNode], order):
            if subroot.val == None:
                return
            Travel(subroot.left, order)
            order.append(subroot.val)
            Travel(subroot.right, order)
        order = []
        Travel(root, order)
        return order