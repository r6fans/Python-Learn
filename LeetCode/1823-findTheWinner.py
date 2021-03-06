#约瑟夫环问题： f(n,k)表示第n个胜利者的下标位置, 则f(n,k)=(f(n-1, k) + k) % n + 1
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if n < 1 or k < 1:
            return -1
        if n == 2:
            if k % 2 == 0:
                return 1
            else:
                return 2
        else:
            return (self.findTheWinner(n - 1, k) + k - 1) % n + 1
    # 迭代
    def findTheWinner_1(self, n: int, k: int) -> int:
        ans = 0
        for i in range(2, n + 1):
            ans = (ans + k) % i
        return ans + 1
        
print(Solution().findTheWinner(10, 20))