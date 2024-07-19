import time 
start_time = time.time()
class Solution:
    def solve(self,n,k,x,dp):
        if x < 0: # target is < 0
            return 0
        
        if n == 0 and x !=0: # target not reached but dice are over
            return 0

        if x == 0 and n !=0: # target reached but dice are still present
            return 0
        
        if n == 0 and x == 0:
            return 1
        
        if dp[n][x] != -1:
            return dp[n][x]
        
        ans = 0
        for i in range(1,k+1):
            ans += self.solve(n-1,k,x-i,dp)
        dp[n][x]= ans
        return dp[n][x]

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[-1 for _ in range(target+1)] for _ in range(n+1)]
        return (self.solve(n,k,target,dp)) % (10 ** 9 + 7)

obj = Solution()
n = 2
k = 6
target = 7

n = 30
k = 30
target = 500
print(obj.numRollsToTarget(n,k,target))
end_time = time.time()
print("Time taken:", end_time - start_time)