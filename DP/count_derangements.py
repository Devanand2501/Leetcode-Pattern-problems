def countDerangements(n,dp):
    if n==1:
        return 0
    if n==2:
        return 1
    if dp[n] != -1:
        return dp[n]
    mod = 10**9 + 7
    dp[n] = (((n - 1) % mod) * ((countDerangements(n - 2,dp) % mod) + (countDerangements(n - 1,dp) % mod)) % mod)
    return dp[n]
t = int(input())
for _ in range(t):
    n = int(input())
    dp = [-1] * (n + 1)
    print(countDerangements(n, dp))