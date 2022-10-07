class Solution:
    #暴力法
    # def search(self, nums: List[int], target: int) -> int:
    #     if target in set(nums):
    #         return nums.index(target)
        
    #     return -1
    
    #二分法
    def search(self, nums: list(int), target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high) / 2
            if ((nums[0] > target) ^ (nums[0] > nums[mid]) ^ (target > nums[mid])):
                low = mid + 1
            else:
                high = mid
        
        return (low == high & low if nums[low] == target else -1)
    

if __name__ == '__main__':
    print(Solution().search([4,5,6,7,0,1,2], 0))
            