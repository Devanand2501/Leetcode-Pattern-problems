def solve(n,k,dp):
        if n==1:
            return k
        if n==2:
            return k*k
        if dp[n] != -1:
            return dp[n]
        mod = 10 **9 + 7
        dp[n]= ((solve(n-2,k,dp)* (k-1))
                + (solve(n-1,k,dp) * (k-1)
                ))%mod
        return dp[n]
def paintFence(n:int,k:int)->int:
    dp = [-1]*(n+1)
    return solve(n,k,dp)


n=2
k = 3
print(paintFence(n,k))