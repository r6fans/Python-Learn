class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        ans, last = [INF] * len(s), -INF
        for i, ch in enumerate(s):
            if ch == c:
                last = i
            ans[i] = min(ans[i], i - last)
        last = inf
        for i, ch in enumerate(s[::-1]):
            if ch == c:
                last = -i
            ans[-1 - i] = min(ans[-1 - i], last + i)
        return ans

s = "loveleetcode"
c = "e"
print(Solution().shortestToChar(s, c))