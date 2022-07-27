class Solution:
    # 动态规划法
    def maxSubArray(self, nums: list[int]) -> int:
        dp = []
        dp.append(nums[0])
        result = dp[0]
        for i in range(1, len(nums)):
            dp.insert(i, max(dp[i - 1] + nums[i], nums[i]))
            result = max(result, dp[i])
        
        return result
    
    # 分治法
    def maxSubArray_fenzhi(self, nums: list[int]) -> int:
        n = len(nums)
        #递归终止条件
        if n == 1:
            return nums[0]
        else:
            #递归计算左半边最大子序和
            max_left = self.maxSubArray(nums[0:len(nums) // 2])
            #递归计算右半边最大子序和
            max_right = self.maxSubArray(nums[len(nums) // 2:len(nums)])
        
        #计算中间的最大子序和，从右到左计算左边的最大子序和，从左到右计算右边的最大子序和，再相加
        max_l = nums[len(nums) // 2 - 1]
        tmp = 0
        for i in range(len(nums) // 2 - 1, -1, -1):
            tmp += nums[i]
            max_l = max(tmp, max_l)
        max_r = nums[len(nums) // 2]
        tmp = 0
        for i in range(len(nums) // 2, len(nums)):
            tmp += nums[i]
            max_r = max(tmp, max_r)
        #返回三个中的最大值
        return max(max_right,max_left,max_l+max_r)

if __name__ == '__main__':
    print(Solution().maxSubArray_fenzhi([5,4,-1,7,8]))
