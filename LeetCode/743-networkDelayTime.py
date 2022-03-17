class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = [[float('inf')] * n for _ in range(n)]
        for x, y, time in times:
            g[x - 1][y - 1] = time

        dist = [float('inf')] * n
        dist[k - 1] = 0
        used = [False] * n
        for _ in range(n):
            x = -1
            for y, u in enumerate(used):
                if not u and (x == -1 or dist[y] < dist[x]):
                    x = y
            used[x] = True
            for y, time in enumerate(g[x]):
                dist[y] = min(dist[y], dist[x] + time)

        ans = max(dist)
        return ans if ans < float('inf') else -1

#领接矩阵

#领接矩阵数组，w[a] [b] = c 代表从A到B有权重为C的边
#加变操作
def add(a,b,c):
    w[a][b] = c

#邻接表
#邻接表与数组存储单链表的实现一致(头插法)，这种存图方式又叫链式前向星图，适用于变数较少的稀疏图使用



#Floyd(邻接矩阵)
def networkDelayTimeFloyd(self, times: List[List[int]], n: int, k: int) -> int:
    #初始化邻接矩阵
    INF = 10 ** 9
    edge = [[]]
