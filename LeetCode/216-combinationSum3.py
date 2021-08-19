class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []
        def backtracking(k,n,sum,startIndex):
            if sum > n:
                return
            if sum == n and len(path) == k:
                return res.append(path[:])
            for i in range(startIndex, 9-(k-len(path)) + 2):
                path.append(i)
                sum += i
                backtracking(n,k,sum,i+1)
                sum -= i
                path.pop()
        backtracking(n,k,0,0)
        return res




