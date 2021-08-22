class Solution:
    def __init__(self) -> None:
        self.board = []

    def isValid(self, row: int, col: int, target: int) -> bool:
        for idx in range(len(self.board)):
            # 同列是否重复
            if self.board[idx][col] == str(target):
                return False
            # 同行是否重复
            if self.board[row][idx] == str(target):
                return False
            # 9宫格里是否重复
            box_row, box_col = (row // 3) * 3 + idx // 3, (col // 3) * 3 + idx % 3
            if self.board[box_row][box_col] == str(target):
                return False
        return True
    
    def getPlace(self) -> List[int]:
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if self.board[row][col] == ".":
                    return [row, col]
        return [-1, -1]
    
    def isSolved(self) -> bool:
        row, col = self.getPlace() # 找个空位置
        
        if row == -1 and col == -1: # 没有空位置，棋盘被填满的
            return True
        
        for i in range(1, 10):
            if self.isValid(row, col, i): # 检查这个空位置放i，是否合适
                self.board[row][col] = str(i) # 放i
                if self.isSolved(): # 合适，立刻返回, 填下一个空位置。
                    return True
                self.board[row][col] = "." # 不合适，回溯
        
        return False # 空位置没法解决

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board is None or len(board) == 0:
            return
        self.board = board
        self.isSolved()
        