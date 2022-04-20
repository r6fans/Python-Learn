class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def dfs(x):
            yield x
            for next in range(x * 10, min(n + 1, (x + 1) * 10)):
                yield from dfs(next)
        array = [v for i in range(1, min(n + 1, 10)) for v in dfs(i)]
        return array[k - 1]


print(Solution().findKthNumber(53,10))