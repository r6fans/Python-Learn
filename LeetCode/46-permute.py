class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = []
        def backtracking(nums,used):
            if len(path) >= len(nums):
                return res.append(path[:])
            for i in range(0, len(nums)):
                if nums[i] == used:
                    continue
                path.append(nums[i])
                used.append(nums[i])
                backtracking(nums,used)
                used.pop()
                path.pop()
        backtracking(nums,used)
        return res