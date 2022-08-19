class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        hashmap = {}
        mid = len(nums) // 2
        
        for i in range(len(nums)):
            if nums[i] in hashmap.keys():
                count = hashmap.get(nums[i])
                count += 1
                hashmap[nums[i]] = count
            else:
                hashmap[nums[i]] = 1
        for k,v in hashmap.items():
            if v > mid:
                return k
             
if __name__ == "__main__":
    print(Solution().majorityElement([6,5,5]))    