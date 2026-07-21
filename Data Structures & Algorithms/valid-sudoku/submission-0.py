class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != ".":
                    row_tag = (val,"row",r)
                    col_tag = (val,"col",c)
                    board_tag = (val,"board",r//3,c//3)
                    if row_tag in seen or col_tag in seen or board_tag in seen:
                        return False
                    seen.add(row_tag)
                    seen.add(col_tag)
                    seen.add(board_tag)
        return True