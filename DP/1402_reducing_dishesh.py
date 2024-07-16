class Solution:
    def solve(self,score, index, time,dp):
        if index == len(score):
            return 0
        if dp[index][time] != -1:
            return dp[index][time]
        inc = score[index] * (time) + self.solve(score,index + 1, time + 1,dp)
        exc = self.solve(score,index + 1, time,dp)
        dp[index][time] = max(inc,exc)
        return dp[index][time]
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        n = len(satisfaction)
        dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
        satisfaction.sort()
        return self.solve(satisfaction,0,1,dp)

obj = Solution()
print(obj.maxSatisfaction([-1,-8,0,5,-9]))