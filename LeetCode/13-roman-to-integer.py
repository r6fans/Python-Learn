class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        romans = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        for i in range(len(s) - 1):
            if romans[s[i]] >= romans[s[i + 1]]:
                sum += romans[s[i]]
            else:
                sum -= romans[s[i]]

        return sum + romans[s[-1]]



