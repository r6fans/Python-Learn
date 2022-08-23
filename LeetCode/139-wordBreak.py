class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = [None]*len(s)

        # 以索引i为起始到末尾的字符串能否由字典组成
        def dfs(i):
            # 长度超过s,返回True(空字符能组成)
            if i >= len(s): 
                return True
            # 存在以i为起始的递归结果
            if memo[i] != None:
                return memo[i]
            # 递归
            for j in range(i,len(s)):
                if s[i:j+1] in wordDict and dfs(j+1):
                    memo[i] = True
                    return True
            memo[i] = False
            return False
        
        return dfs(0)