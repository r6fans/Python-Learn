class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans, left, cur = 0, 0, 1
        for right, num in enumerate(nums):
            cur *= num
            # 当前到右指针的连乘太大，需要一直挪动左指针直到小于k
            while left <= right and cur >= k:
                cur //= nums[left]
                left += 1
            # 在left到right之间的i, nums[i:right+1]的连乘都满足小于k
            ans += right - left + 1
        return ans

print(Solution().numSubarrayProductLessThanK([10,5,2,6], 100))