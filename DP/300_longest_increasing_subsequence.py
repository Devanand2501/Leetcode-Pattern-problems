class Solution:
    def solve(self,nums,curidx,previdx):
        if curidx==len(nums):
            return 0
        inc = 0
        if previdx == -1 or nums[curidx]>nums[previdx]:
            inc = 1 + self.solve(nums,curidx+1,curidx)
        exc = self.solve(nums,curidx+1,previdx)
        return max(exc,inc)
    def lengthOfLIS(self, nums: list[int]) -> int:
        return self.solve(nums,0,-1)

obj = Solution()
nums = [10,9,2,5,3,7,101,18]
print(obj.lengthOfLIS(nums))