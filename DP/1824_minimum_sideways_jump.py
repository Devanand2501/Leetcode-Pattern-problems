class Solution:
    def solve(self,obs, currlane, currpos):
        if currpos == len(obs)-1:
            return 0
        if obs[currpos + 1] != currlane:
            return self.solve(obs,currlane,currpos+1)
        else:
            ans = float("inf")
            for i in range(1,4):
                if currlane != i and obs[currpos] != i :
                    ans = min(ans, 1 + self.solve(obs,i,currpos+1))
            return ans 

    def minSideJumps(self, obstacles: list[int]) -> int:
        return self.solve(obstacles,2,0)

obj = Solution()
obstacles = [0,1,2,3,0]
print(obj.minSideJumps(obstacles))