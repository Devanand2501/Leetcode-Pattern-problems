class Solution:
    ''' PREVIOUSLY OPTIMIZED SOLUTION
    def solve(self,k,prices):
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

    def maxProfit(self, k: int, prices: List[int]) -> int:
        return self.solve(prices,k)
    '''
    def solve(self,k,prices,index,operation_num):
        if index==len(prices):
            return 0
        if operation_num == 2*k:
            return 0
        profit = 0
        if operation_num%2==0:
            buy_karo = -prices[index] + self.solve(k,prices,index+1,operation_num+1)
            skip_karo = 0 + self.solve(k,prices,index+1,operation_num)
            profit = max(buy_karo,skip_karo)
        else:
            sell_karo = prices[index] + self.solve(k,prices,index+1,operation_num+1)
            skip_karo = 0 + self.solve(k,prices,index+1,operation_num)
            profit = max(sell_karo,skip_karo)
        return profit

    def maxProfit(self, k: int, prices: list[int]) -> int:
        return self.solve(k,prices,0,0)

obj = Solution()
k = 2
prices = [3,2,6,5,0,3]
print(obj.maxProfit(prices,k))  