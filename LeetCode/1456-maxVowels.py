class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def isYuan(s):
            vowels = ["a", "e", "i", "o", "u"]
            return 1 if s in vowels else 0
        right, sum, max =0
        while right < len(s) - 1:
            sum += isYuan(s[right])
            right += 1
            if right >= k:
                max = max(max,sum)
                sum -= isYuan(s[right - k])
        return max
