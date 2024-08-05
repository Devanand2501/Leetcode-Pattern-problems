class Solution:
    def solve(self,grid,n,k,memo):
        if n== 0 and k==0 :
            return 0
        if n== 0 or k==0 :
            return -float("inf")
        if (n,k) in memo:
            return memo[(n,k)]
        maxx = -float("inf")
        for i in range(n):
            maxx = max(maxx,self.solve(grid,i,k-1,memo) + grid[i][n-1])
        memo[(n,k)] = maxx
        return memo[(n,k)]
    def largestSumOfAverages(self, nums: list[int], k: int) -> float:
        n = len(nums)
        grid = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n-1,i-1,-1):
                grid[i][j] = sum(nums[i:j+1])/(j-i+1)
        # print(grid)
        n = len(grid)
        memo = {}
        return self.solve(grid,n,k,memo)

nums = [9,1,2,3,9]
k = 3
obj = Solution()
print(obj.largestSumOfAverages(nums,k))
