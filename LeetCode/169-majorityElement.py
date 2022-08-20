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
    
    def majityElement_moore(self, nums: list[int]) -> int:
        major = 0
        count = 0
        
        for n in nums:
            if count == 0:
                major = n
            if n == major:
                count = count + 1
            else:
                count = count - 1

        return major
             
if __name__ == "__main__":
    print(Solution().majorityElement([6,5,5]))    