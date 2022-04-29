class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        for item in range(0,len(nums)):
            if nums[item] % 2 == 0:
                odd.append(nums[item])
            else:
                even.append(nums[item])
        return odd + even

# 双指针
