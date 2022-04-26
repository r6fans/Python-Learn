class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        return sum(sum(v > 0 for v in g) + max(g) for g in grid) + sum(max(g) for g in zip(*grid))