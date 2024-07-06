class Solution:
    def solve(self,nums,target,dp):
        if target==0:
            return 1
        if target <0:
            return 0
        if dp[target] != 0:
            return dp[target]
        count = 0
        for i in nums:
            dp[target] += self.solve(nums,target-i,dp)
        return dp[target]
    def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target+1)
        ans = self.solve(nums,target,dp)
        return ans

obj = Solution()
nums = [1,2]
target = 3
print(obj.combinationSum4(nums, target))