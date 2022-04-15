class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        MAX_LINE=100
        lines, cur = 1,0
        for item in s:
            item_width = widths[ord(item) - ord('a')]
            if cur + item_width >= MAX_LINE:
                lines += 1
                cur = item_width
            else:
                cur += item_width
        return [lines, cur]