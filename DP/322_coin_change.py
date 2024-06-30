class Solution:
    ''' RECURSION
    def solve1(self,coins,amount):
        if amount == 0:
            return 0
        if amount <0:
            return 10e7
        mini = 10e7
        for i in coins:
            ans = self.coinChange(coins,amount-i)
            if ans != -1:
                mini = min(mini,ans+1)
        return mini
    '''
    
    ''' TOP-DOWN
    def solve2(self,coins,amount,dp):
        if amount == 0:
            return 0
        if amount <0:
            return 10e7
        if dp[amount] != -1:
            return dp[amount]
        mini = 10e7
        for i in coins:
            ans = self.solve2(coins,amount-i,dp)
            if ans != -1:
                mini = min(mini,ans+1)
        dp[amount]= mini
        return dp[amount]
    '''
    
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [-1]*(len(coins)+1)
        ans = self.solve2(coins,amount,dp)
        if ans == 10e7:
            return -1
        else:
            return ans

obj = Solution()
coins = [1,2,5]
amount = 11
print(obj.coinChange(coins, amount))