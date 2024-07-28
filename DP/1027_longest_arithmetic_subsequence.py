class Solution:
    def solve(self,i,diff,nums,dp):
        if i<0:
            return 0
        if (i,diff) in dp:
            return dp[(i,diff)]
        ans = 0
        for j in range(i-1,-1,-1):
            if nums[i] - nums[j] == diff:
                ans = max(ans,1 + self.solve(j,diff,nums,dp))
        dp[(i,diff)]= ans
        return dp[(i,diff)]
    def longestArithSeqLength(self, nums: list[int]) -> int:
        n = len(nums)
        if n<=2:
            return n
        dp = {}
        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                diff = nums[j] - nums[i]
                ans = max(ans,2 + self.solve(i,diff,nums,dp))
        return ans

obj = Solution()
nums = [3,6,9,12]
print(obj.longestArithSeqLength(nums))  