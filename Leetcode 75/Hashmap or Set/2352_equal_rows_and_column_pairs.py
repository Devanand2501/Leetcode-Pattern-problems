class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        n = len(grid)
        # j=0
        count = 0
        for i in range(n):
            j = 0
            while j<n:
                if grid[i] == [x[j] for x in grid]:
                    count+=1
                j+=1
        return count

obj = Solution()
grid = [[3,2,1],[1,7,6],[2,7,7]]
grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
print(obj.equalPairs(grid))

# print([x[0] for x in grid ])
# for x in grid:
#     print(x[:][0])
