class Solution:
    def solve(self,prices,k):
        curr = [[0 for _ in range(k+1)] for _ in range(2)]
        next = [[0 for _ in range(k+1)] for _ in range(2)]
        for index in range(len(prices)-1,-1,-1):
            for can_buy in range(2):
                for limit in range(1,k+1):
                    profit = 0
                    if can_buy:
                        buy_karo = -prices[index] + next[0][limit]
                        skip_karo = 0 + next[1][limit]
                        profit = max(buy_karo,skip_karo)
                    else:
                        sell_karo = prices[index] + next[1][limit-1]
                        skip_karo = 0 + next[0][limit]
                        profit = max(sell_karo,skip_karo)
                    curr[can_buy][limit] = profit
            next = curr[:]
        return next[can_buy][limit]

    def maxProfit(self, prices: list[int],k:int) -> int:
        return self.solve(prices,k)

obj = Solution()
k = 2
prices = [3,2,6,5,0,3]
print(obj.maxProfit(prices,k))  