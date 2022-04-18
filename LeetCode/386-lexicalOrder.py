class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        def dfs(x):
            yield x
            for next in range(x * 10, min(n + 1, (x + 1) * 10)):
                yield from dfs(next)
        return [v for i in range(1, min(n + 1, 10)) for v in dfs(i)]


print(Solution().lexicalOrder(20))