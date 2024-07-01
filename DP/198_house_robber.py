class Solution:
    def solve(self,nums,n,dp):
        if n<0:
            return 0
        if n==0:
            return nums[0]
        if dp[n]!=-1:
            return dp[n]
        inc = self.solve(nums,n-2,dp) + nums[n]
        exc = self.solve(nums,n-1,dp) 
        dp[n] = max(inc,exc)
        return dp[n]
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        return self.solve(nums,n-1,dp)

obj = Solution()
nums = [1,2,3,1]
print(obj.rob(nums))