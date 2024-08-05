class Solution:
    def solve(self,grid,n,k):
        if n== 0 and k==0 :
            return 0
        if n== 0 or k==0 :
            return -float("inf")
        maxx = -float("inf")
        for i in range(n):
            maxx = max(maxx,self.solve(grid,i,k-1) + grid[i][n-1])
        return maxx
    def largestSumOfAverages(self, nums: list[int], k: int) -> float:
        n = len(nums)
        grid = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n-1,i-1,-1):
                grid[i][j] = sum(nums[i:j+1])/(j-i+1)
        print(grid)
        n = len(grid)
        return self.solve(grid,n)

nums = [9,1,2,3,9]
k = 3
obj = Solution()
print(obj.largestSumOfAverages(nums,k))
