class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for i in range(len(nums)):
            result ^= nums[i]
        return result 
            

if __name__ == '__main__':
    print(Solution().singleNumber([4,1,2,1,2]))