class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a = []
        for i in range(0,len(nums) - 1):
            a[i] = nums[i] * nums[i]
        return sorted(a)
            