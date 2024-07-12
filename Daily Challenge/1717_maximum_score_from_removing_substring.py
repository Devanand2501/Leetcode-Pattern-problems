class Solution:
    def solve(self,s,x,y,dp):
        if s.find("ab") == -1 and s.find("ba") == -1:
            return 0
        indexab = s.find("ab")
        indexba = s.find("ba")
        ab = 0
        ba = 0
        if s in dp:
            return dp[s]
        if indexab != -1:
            ab = self.solve(s[:indexab]+s[indexab+2:],x,y,dp) + x
        if indexba != -1:
            ba = self.solve(s[:indexba]+s[indexba+2:],x,y,dp) + y
        dp[s] = max(ab,ba)
        return dp[s]
    def maximumGain(self, s: str, x: int, y: int) -> int:
        dp = {}
        return self.solve(s,x,y,dp)

s = "aabbaaxybbaabb"
x = 5
y = 4
print(Solution().maximumGain(s,x,y))