class Solution:
    def solve(self,obs, currlane, currpos,dp):
        if currpos == len(obs)-1:
            return 0
        if dp[currlane][currpos] != -1 :
            return dp[currlane][currpos]
        if obs[currpos + 1] != currlane:
            return self.solve(obs,currlane,currpos+1,dp)
        else:
            ans = float("inf")
            for i in range(1,4):
                if currlane != i and obs[currpos] != i :
                    ans = min(ans, 1 + self.solve(obs,i,currpos+1,dp))
            dp[currlane][currpos] = ans 
            return dp[currlane][currpos]

    def minSideJumps(self, obstacles: list[int]) -> int:
        dp = [[-1 for _ in range(len(obstacles)) ] for _ in range(4)]
        return self.solve(obstacles,2,0,dp)

obj = Solution()
obstacles = [0,1,2,3,0]
print(obj.minSideJumps(obstacles))