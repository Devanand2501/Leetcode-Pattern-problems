class Solution:
    def solve(self,matrix,maxx,i,j,dp):
        if (i>=len(matrix) or j>=len(matrix[0])):
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        diagonal = self.solve(matrix,maxx,i+1,j+1,dp)
        bottom = self.solve(matrix,maxx,i+1,j,dp)
        right = self.solve(matrix,maxx,i,j+1,dp)
        if matrix[i][j] == "1":
            dp[i][j] = 1 + min(diagonal,min(bottom,right))
            maxx[0] = max(dp[i][j],maxx[0])
            return dp[i][j] 
        else:
            dp[i][j]=0 
            return dp[i][j]

    def maximalSquare(self, matrix: list[list[str]]) -> int:
        maxx = [0]
        dp = [[-1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        self.solve(matrix,maxx ,0,0,dp)
        return maxx[0] * maxx[0]
        

obj = Solution()
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(obj.maximalSquare(matrix))