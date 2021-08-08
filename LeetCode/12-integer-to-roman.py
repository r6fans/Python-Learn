class Solution:
    def intToRoman(self, num: int) -> str:
        Romans = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX',
                  5: 'V', 4: 'IV', 1: 'I'}
        res = ''
        for keys in Romans:
            if num // keys != 0:
                count = num // keys
                res += Romans[keys] * count
                num %= keys
        return res


if __name__ == '__main__':
    print(Solution().intToRoman(18000))
