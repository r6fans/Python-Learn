class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left,right + 1):
            tmp, flag = i, True
            while tmp and flag:
                flag = not ((t := tmp % 10) == 0 or i % t != 0)
                tmp //= 10
            if flag:
                ans.append(i)
        return ans