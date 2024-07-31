class Solution:
    def solve(self,prices,index,can_buy):
        if index == len(prices):
            return 0
        profit = 0
        if can_buy:
            buy_karo = -prices[index] + self.solve(prices,index+1,0)
            skip_karo = 0 + self.solve(prices,index+1,1)
            profit = max(buy_karo,skip_karo)
        else:
            sell_karo = prices[index] + self.solve(prices,index+1,1)
            skip_karo = 0 + self.solve(prices,index+1,0)
            profit = max(sell_karo,skip_karo)
        return profit
    def maxProfit(self, prices: list[int]) -> int:
        return self.solve(prices,0,1)


obj = Solution()
print(obj.maxProfit([7,1,5,3,6,4]))  