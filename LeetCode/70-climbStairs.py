class Solution:
    def climbStairs(self, n: int) -> int:
        dp = []
        dp.insert(0,1)
        dp.insert(1,1)
        for i in range(2, n + 1):
            dp.insert(i, dp[i - 1] + dp[i - 2])
        return dp[n]