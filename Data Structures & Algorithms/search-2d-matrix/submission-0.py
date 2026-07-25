class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i=0
        while i < len(matrix):
            l = 0
            r = len(matrix[i])-1
            while l<= r:
                if target > matrix[i][r]:
                    i+=1
                    break
                if target < matrix[i][l]:
                    return False
                mid = (l+r) // 2
                current = matrix[i][mid]
                if(target > current):
                    l= mid +1
                elif(target < current):
                    r = mid - 1
                elif(target == current):
                    return True
        return False
        


