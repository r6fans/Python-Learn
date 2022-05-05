class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        win = []
        left, right = 0,0
        ans = 0
        cur = 1
        while right < len(nums) - 1:
            win.append(nums[right])
            right += 1
            cur = cur * nums[right]
            while cur >= k:
                ans += 1
                left += 1
        return ans

print(Solution().numSubarrayProductLessThanK([10,5,2,6], 100))