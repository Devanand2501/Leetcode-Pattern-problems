class Solution:
    def solve(self,n,dp):
        if n==0:
            return 0
        if dp[n] != -1:
            return dp[n]
        ans = n
        i =1
        while i*i<=n:
            ans = min(1+self.solve(n-i**2,dp),ans)
            i+=1
        dp[n] = ans
        return dp[n]
    def numSquares(self, n: int) -> int:
        dp = [-1] * (n+1)
        return self.solve(n,dp)

obj = Solution()
print(obj.numSquares(12))