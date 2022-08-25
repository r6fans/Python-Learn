class Solution:
    def productExceptSelf(self, nums):
        ans = []
        for i in range(len(nums)):
            tem = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                tem = tem * nums[j]
            ans.append(tem)
        
        return ans

if __name__ == '__main__':
    print(Solution().productExceptSelf([1,2,3,4]))