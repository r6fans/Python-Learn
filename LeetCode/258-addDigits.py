class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            t = 0
            while num != 0:
                t += num % 10
                num /= 10
            num = t
        return t