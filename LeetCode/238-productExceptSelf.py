class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)

        L = [0] * (length + 10)
        R = [0] * (length + 10)

        L[0] = 1

        R[length + 1] = 1

        for i in range(1, length):
            L[i] = L[i-1] * nums[i - 1]
        
        for j in range(length, -1, -1):
            R[j] = R[j + 1] * nums[j - 1]
        
        return [L[i - 1] * R[i + 1] for i in range(1, length + 1)]




if __name__ == '__main__':
    print(Solution().productExceptSelf([1,2,3,4]))