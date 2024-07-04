class Solution:
    def solve(self,capacity, wt,value,index,dp):
        if index == 0:
            if wt[0]<=capacity:
                return val[0]
            else:
                return 0
        if dp[index][capacity] != -1:
            return dp[index][capacity]
        inc = 0
        if wt[index]<=capacity:
            inc = self.solve(capacity-wt[index], wt,value,index-1,dp) + value[index]
        exc = self.solve(capacity, wt,value,index-1,dp) + 0
        dp[index][capacity] = max(inc,exc)
        return dp[index][capacity]

    def knapSack(self,W, wt, val, n):
        dp = [[-1 for _ in range(W + 1)] for _ in range(n)]
        return self.solve(W,wt,val,n-1,dp)

n=3
capacity=4
wt=[4,5,1]
val=[1,2,3]
obj = Solution()
print(obj.knapSack(capacity,wt,val,n))