class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        left = []
        right = []
        for i in range(0, len(s)):
            temp = []
            for j in range(0, len(s)):
                if s[j] == 'c':
                    str_len = j - i 
                    temp.append(abs(str_len))
            left.append(min(temp))
            
            for j in range(0, len(s)):
                if s[::-1][j] == 'c':
                    str_len = j - i 
                    temp.append(abs(str_len))
            right.append(min(temp))
            
        return [min(left[i],right[i]) for i in range(0, len(s))]

s = "loveleetcode"
c = "e"
print(Solution().shortestToChar(s, c))