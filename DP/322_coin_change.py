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
    def coinChange(self, coins: list[int], amount: int) -> int:
        ans = self.solve1(coins,amount)
        if ans == 10e7:
            return -1
        else:
            return ans

obj = Solution()
coins = [1,2,5]
amount = 11
print(obj.coinChange(coins, amount))