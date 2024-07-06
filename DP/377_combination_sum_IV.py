class Solution:
    def solve(self,nums,target,dp):
        if target <0:
            return 0
        if target==0:
            return 1
        if dp[target] != -1:
            return dp[target]
        count = 0
        for i in nums:
            count += self.solve(nums,target-i,dp)
        dp[target] = count
        return dp[target]
    def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [-1] * (target+1)
        ans = self.solve(nums,target,dp)
        return ans

obj = Solution()
nums = [1,2]
target = 3
print(obj.combinationSum4(nums, target))