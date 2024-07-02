def solve(n,x,y,z,dp):
    if n==0:
        return 0
    if n<0:
        return float('-inf')
    if dp[n] != -1:
        return dp[n]
    a = solve(n-x,x,y,z,dp)
    b = solve(n-y,x,y,z,dp)
    c = solve(n-z,x,y,z,dp)
    dp[n] = max(a,max(b,c)) +1
    return dp[n]
def cutSegments(n, x, y, z):
    dp = [-1] * (n+1)
    ans = solve(n,x,y,z,dp)
    if ans <0:
        return 0
    else:
        return ans

print(cutSegments(7,5,2,2))