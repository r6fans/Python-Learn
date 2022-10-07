# 动态规划-背包问题
# 什么是背包问题？
# 给定一个背包容量target, 再给定一个物品数组nums, 能否按照一定的选取规则来从物品数组nums得到背包容量target
# 背包问题分类
# 1. 0/1背包： 每个元素最多选取一次
# 2. 完全背包： 每个元素可以重复选取
# 3. 组合背包： 背包中的物品需要考虑顺序
# 4. 分组背包问题： 不止一个背包，需要遍历每个背包
# 背包问题的要求分类：
# 1. 最值问题： 要求最大/最小值
# 2. 存在问题： 是否存在...., 满足...
# 3. 组合问题： 求所有满足.....的排列组合

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = []
        dp.append(0)
        for item in range(len(amount) + 1):
            for coin in coins:
                if (item - coin) < 0:
                    continue
                dp.append(min(dp[item],1 + dp[item - coin]))
        return -1 if dp[amount] == amount + 1 else dp[amount]
        