class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # iterate through rows check if contain dupl
        for row in board:
            if self.valid(row) == False:
                return False
        n = len(board[0])

        # get cols
        cols = []

        for c in range(n):
            col = []
            for r in range(n):
                col.append(board[r][c])
            cols.append(col)
        
        # iterate through cols check if contain dupl
        for col in cols:
            if self.valid(col) == False:
                return False
        
        # get grid
            # split each row into left, mid, right based on 0:2, 2:5, 5:8
        grid =[]
        for i in range(0, 9, 3): 
            left = []
            right = []
            mid = []
            for j in range(i, i+3, 1):
                row = board[j]
                left.extend(row[0:3])
                mid.extend(row[3:6])
                right.extend(row[6:])
            grid.append(left)
            grid.append(mid)
            grid.append(right)

        # iterate through grid
        for row in grid:
            if self.valid(row) == False:
                return False

        return True


    def valid(self, nums):
        digits=[]
        for char in nums:
            if char.isdigit():
                digits.extend(char)
        return len(digits) == len(set(digits))