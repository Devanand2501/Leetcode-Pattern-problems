class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(n):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        return -1

obj = Solution()
nums = [4,1,4]
nums = [1,7,3,6,5,6]
nums = [1,2,3]
print(obj.pivotIndex(nums))