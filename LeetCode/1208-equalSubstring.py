class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left, right, sum= 0, 0, 0
        for right in range(len(s) - 1):
            sum += abs(ord(s[right]) - ord(t[right]))
            if sum > maxCost:
                sum -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            return len(s) - left