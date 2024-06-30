class Solution:
    def solve(self,cost,n,dp):
        if n == 0:
            dp[n]=0
            return cost[0]
        if n == 1:
            dp[n]=1
            return cost[1]
        if dp[n] != -1:
            return dp[n]
        dp[n] = min(self.solve(cost,n-1,dp),self.solve(cost,n-2,dp))+cost[n]
        return dp[n]

    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        dp = [-1] *(n+1)
        return min(self.solve(cost,n-1,dp),self.solve(cost,n-2,dp))

obj = Solution()
cost = [10,15,20]
print(obj.minCostClimbingStairs(cost))