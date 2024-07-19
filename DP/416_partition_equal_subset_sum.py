class Solution:
    ''' RECURSION
    def solve(self,nums,index,target):
        if index == len(nums):
            return 0
        if target<0:
            return 0
        if target == 0:
            return 1
        inc = self.solve(nums,index+1,target-nums[index])
        exc = self.solve(nums,index+1,target)
        return inc or exc
    def canPartition(self, nums: list[int]) -> bool:
        n = len(nums)
        if sum(nums) % 2 == 1:
            return False
        return self.solve(nums,0,sum(nums)//2)
    '''
    def solve(self,nums,index,target,dp):
        if index == len(nums):
            return 0
        if target<0:
            return 0
        if target == 0:
            return 1
        if dp[index][target] != -1:
            return dp[index][target]
        inc = self.solve(nums,index+1,target-nums[index],dp)
        exc = self.solve(nums,index+1,target,dp)
        dp[index][target] = inc or exc
        return dp[index][target]
    def canPartition(self, nums: list[int]) -> bool:
        n = len(nums)
        target = sum(nums)//2
        if sum(nums) % 2 == 1:
            return False
        dp = [[-1 for _ in range(target + 1)] for _ in range(n + 1 )]
        return self.solve(nums,0,target,dp)

obj = Solution()
nums = [1,5,11,5]
print(obj.canPartition(nums))