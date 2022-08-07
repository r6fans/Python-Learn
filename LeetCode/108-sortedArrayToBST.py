# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:


        return self.makeTree(0, len(nums) - 1, nums)

    def makeTree(self, left_index, right_index, nums):
        if left_index > right_index:
            return None
        
        mid = (right_index - left_index) // 2

        tree = TreeNode(nums[mid])
        tree.left = self.makeTree(left_index, mid - 1, nums)
        tree.right = self.makeTree(mid + 1, right_index, nums)

        return tree


        