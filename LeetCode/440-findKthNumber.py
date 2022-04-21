class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # 小于等于n的以1开头的数有多少个?
        # 1 10-19 100-199 1000-1999 = 1111
        def dfs(l, r):
            # 当前层有 r - l + 1 个节点可取，递归到下一层。
            # l * 10： 从10变成100， r * 10 + 9: 从19变成199
            return 0 if l > n else min(n, r) - l + 1 + dfs(l * 10, r * 10 + 9)
        
        cur = 1
        k -= 1
        while k:
            cnts = dfs(cur, cur)
            # 当前节点中总数都小于需要的数，可以全部取走，bfs到同层下一点 (比如 1 -> 2)
            if cnts <= k:
                k -= cnts
                cur += 1
            # 答案在当前节点的子节点中，取走当前根节点，dfs向下 (比如 1 -> 10)
            else:
                k -= 1
                cur *= 10
        return cur


print(Solution().findKthNumber(53,10))