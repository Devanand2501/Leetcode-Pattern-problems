class Solution:
    def solve(self, nums, i, n,dp):
        if i >= n - 1:
            return 0
        if dp[i] != float("inf"):
            return dp[i]
        min_jumps = float('inf')
        
        for j in range(1, nums[i] + 1):
            if i + j < n:
                jumps = self.solve(nums, i + j, n,dp)
                if jumps != float('inf'):
                    min_jumps = min(min_jumps, jumps + 1)
        dp[i]= min_jumps
        return dp[i]

    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [float('inf')]*(n)
        if n == 0:
            return 0
        return self.solve(nums, 0, n,dp)

obj = Solution()
nums = [2,3,1,1,4]
print(obj.jump(nums))