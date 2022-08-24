class Solution:
    def productExceptSelf(self, nums):
        ans = []

        for i in range(len(nums)):
            new = nums
            del new[i]
            tem = 1
            for j in range(len(new)):
                tem = tem * new[j]
            ans.append(tem)
        
        return ans

if __name__ == '__main__':
    print(Solution().productExceptSelf([1,2,3,4]))