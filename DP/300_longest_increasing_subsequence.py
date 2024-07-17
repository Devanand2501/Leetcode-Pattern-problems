class Solution:
    def solve(self,nums,curidx,previdx,dp):
        if curidx==len(nums):
            return 0
        if dp[curidx][previdx]!=-1:
            return dp[curidx][previdx]
        inc = 0
        if previdx == -1 or nums[curidx]>nums[previdx]:
            inc = 1 + self.solve(nums,curidx+1,curidx,dp)
        exc = self.solve(nums,curidx+1,previdx,dp)
        dp[curidx][previdx] = max(inc,exc)
        return dp[curidx][previdx]
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [[-1 for _ in range(len(nums)+1)] for _ in range(len(nums))]
        return self.solve(nums,0,-1,dp)

obj = Solution()
nums  = [0,1,0,3,2,3]
print(obj.lengthOfLIS(nums))