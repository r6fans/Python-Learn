class Solution:
    def rob(self, nums: List[int]) -> int:
        lin1, lin2 = 0,0
        for price1 in nums[::2]:
            lin1 += price1
        for price2 in nums[1::2]:
            lin2 += price2
        return max(lin1,lin2)