# 动态规划法
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        dp = []
        dp.append(nums[0])
        result = dp[0]
        for i in range(1, len(nums)):
            dp.insert(i, max(dp[i - 1] + nums[i], nums[i]))
            result = max(result, dp[i])
        
        return result



if __name__ == '__main__':
    print(Solution().maxSubArray([5,4,-1,7,8]))
