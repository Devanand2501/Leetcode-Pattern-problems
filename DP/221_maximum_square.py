class Solution:
    def solve(self,matrix,maxx,i,j):
        if (i>=len(matrix) or j>=len(matrix[0])):
            return 0
        diagonal = self.solve(matrix,maxx,i+1,j+1)
        bottom = self.solve(matrix,maxx,i+1,j)
        right = self.solve(matrix,maxx,i,j+1)
        if matrix[i][j] == "1":
            ans = 1 + min(diagonal,min(bottom,right))
            maxx[0] = max(ans,maxx[0])
            return ans 
        else:
            return 0    

    def maximalSquare(self, matrix: list[list[str]]) -> int:
        maxx = [0]
        self.solve(matrix,maxx ,0,0)
        return maxx[0]
        

obj = Solution()
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(obj.maximalSquare(matrix))