def countDerangements(n,dp):
    ''' RECURSION + MEMOIZATION
    if n==1:
        return 0
    if n==2:
        return 1
    if dp[n] != -1:
        return dp[n]
    mod = 10**9 + 7
    dp[n] = (((n - 1) % mod) * ((countDerangements(n - 2,dp) % mod) + (countDerangements(n - 1,dp) % mod)) % mod)
    return dp[n]
    '''
    if n==1:
        return 0
    if n==2:
        return 1
    mod = 10**9 + 7
    dp = [0]* (n+1)
    dp[1] = 0
    dp[2] = 1
    for i in range(3,n+1):  
        first = dp[i-1] % mod
        second = dp[i-2] % mod
        add = (first + second) %mod
        ans = (i-1  * add)%mod
        dp[i] = ans
    return dp[n]

t = int(input())
for _ in range(t):
    n = int(input())
    dp = [-1] * (n + 1)
    print(countDerangements(n, dp))