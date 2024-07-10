class Solution:
    def solve(self,n,days,cost,index):
        if index>=n:
            return 0
        
        # 1 Day pass 
        oneDay = self.solve(n,days,cost,index+1) + cost[0]
        
        i = index
        while i<n and days[i]<days[index] + 7:
            i+=1
        
        # 7 Days pass
        sevenDay = self.solve(n,days,cost,i) + cost[1]
        
        i = index
        while i<n and days[i]<days[index] + 30:
            i+=1
        
        # 30 Days pass
        thirtyDay = self.solve(n,days,cost,i) + cost[2]

        return min(oneDay,min(sevenDay,thirtyDay))

    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        return self.solve(len(days),days,costs,0)


obj = Solution()
days = [2,5]
costs = [1,4,25]
print(obj.mincostTickets(days, costs))