import heapq
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        ans = []
        window = nums[:k]
        ans.append(max(window))
        for i in range(k,n):
            window = window[1:]
            heapq.heappush(window,nums[i])
            ans.append(max(window))
        print(ans)
        return ans


obj = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(obj.maxSlidingWindow(nums, k))  