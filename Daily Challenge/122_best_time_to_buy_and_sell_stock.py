class Solution:
    def solve(self,prices,index,can_buy,memo):
        if index == len(prices):
            return 0
        if memo[index][can_buy] != -1:
            return memo[index][can_buy]
        profit = 0
        if can_buy:
            buy_karo = -prices[index] + self.solve(prices,index+1,0,memo)
            skip_karo = 0 + self.solve(prices,index+1,1,memo)
            profit = max(buy_karo,skip_karo)
        else:
            sell_karo = prices[index] + self.solve(prices,index+1,1,memo)
            skip_karo = 0 + self.solve(prices,index+1,0,memo)
            profit = max(sell_karo,skip_karo)
        memo[index][can_buy] = profit
        return memo[index][can_buy]
    def maxProfit(self, prices: list[int]) -> int:
        memo = [[-1 for _ in range(2)] for _ in range(len(prices))]
        return self.solve(prices,0,1,memo)


obj = Solution()
print(obj.maxProfit([7,1,5,3,6,4]))  