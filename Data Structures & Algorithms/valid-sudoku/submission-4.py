class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        grid = [set() for _ in range(9)]
        # traverse through board and in one pass, check for duplicates
        for c in range(9):
            for r in range(9):
                val = board[r][c]
                grid_index = ((r // 3) * 3 + (c // 3))
                if val.isdigit():
                    if val in cols[c]:
                        return False
                    if val in rows[r]:
                        return False
                    if val in grid[grid_index]:
                        return False
                    cols[c].add(val)
                    rows[r].add(val)
                    grid[grid_index].add(val)
        return True
