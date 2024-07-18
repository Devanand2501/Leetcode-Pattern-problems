class Solution:
    def solve(self,index,n,slices,end_index,dp):
        if n==0 or index >end_index:
            return 0
        if dp[index][n] != -1:
            return dp[index][n]
        incl = slices[index] + self.solve(index+2,n-1,slices,end_index,dp)
        excl = 0 + self.solve(index+1,n,slices,end_index,dp)
        dp[index][n] = max(incl,excl)
        return dp[index][n]
    def maxSizeSlices(self, slices: list[int]) -> int:
        n = len(slices)
        dp1 = [[-1 for _ in range(n)] for _ in range(n)]
        inc = self.solve(0,n//3,slices,n-2,dp1)
        dp2 = [[-1 for _ in range(n)] for _ in range(n)]
        exc = self.solve(1,n//3,slices,n-1,dp2)
        return max(inc,exc)


obj = Solution()
slices = [1,2,3,4,5,6]
print(obj.maxSizeSlices(slices))