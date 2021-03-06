class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            t = 0
            while num != 0:
                t += (num % 10)
                num = num // 10
            num = t
        return num

    def addDigits2(self, num: int) -> int:
        return (num - 1) % 9 + 1