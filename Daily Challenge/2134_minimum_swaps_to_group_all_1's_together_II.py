class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        n = len(nums)
        total = nums.count(1)
        nums += nums[:total-1]
        # print(nums)
        window = nums[:total] 
        
        swaps = total - window.count(1)
        for i in range(1, n):
            print(window,"swaps-->",swaps)
            window = window[1:] + [nums[i + total - 1]]
            swaps = min(swaps,total - window.count(1))
        return swaps
        

obj = Solution()
nums = [0,1,1,1,0,0,1,1,0]
# nums = [0,1,0,1,1,0,0]
# nums = [1,1,0,0,1]
print(obj.minSwaps(nums)) 