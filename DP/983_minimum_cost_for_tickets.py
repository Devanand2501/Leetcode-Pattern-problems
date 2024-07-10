class Solution:
    def solve(self,n,days,cost,index,dp):
        if index>=n:
            return 0
        
        if dp[index] != -1:
            return dp[index]
        
        # 1 Day pass 
        oneDay = self.solve(n,days,cost,index+1,dp) + cost[0]
        
        i = index
        while i<n and days[i]<days[index] + 7:
            i+=1
        
        # 7 Days pass
        sevenDay = self.solve(n,days,cost,i,dp) + cost[1]
        
        i = index
        while i<n and days[i]<days[index] + 30:
            i+=1
        
        # 30 Days pass
        thirtyDay = self.solve(n,days,cost,i,dp) + cost[2]

        dp[index] =  min(oneDay,min(sevenDay,thirtyDay))
        return dp[index]

    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        n = len(days)
        dp = [-1] * (n+1)
        return self.solve(n,days,costs,0,dp)


obj = Solution()
days = [2,5]
costs = [1,4,25]
print(obj.mincostTickets(days, costs))