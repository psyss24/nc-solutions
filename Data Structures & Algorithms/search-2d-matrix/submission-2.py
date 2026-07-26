class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # perform binary search on entire matrix treating it as a single array
        # can index into particular item by doing:
            # row = index // COLS
            # col = index % COLS
            l=0
            ROWS = len(matrix)
            COLS = len(matrix[0])
            r=ROWS * COLS -1
            while l<= r:
                mid = (l+r) // 2
                row = mid // COLS
                col = mid % COLS
                middle = matrix[row][col]

                if(target == middle):
                    return True
                elif(target>middle):
                    l=mid + 1
                elif(target<middle):
                    r= mid -1
            return False
                