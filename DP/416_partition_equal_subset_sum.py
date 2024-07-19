class Solution:
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

obj = Solution()
nums = [1,5,11,5]
print(obj.canPartition(nums))