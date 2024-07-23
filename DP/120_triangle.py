class Solution:
    def solve(self,triangle,row,i):
        if i==len(triangle[row]):
            return 0
        if row==len(triangle)-1:
            return triangle[row][i]
        else:
            return triangle[row][i]+min(self.solve(triangle,row+1,i),self.solve(triangle,row+1,i+1))

    def minimumTotal(self, triangle: list[list[int]]) -> int:
        return self.solve(triangle,0,0)

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(Solution().minimumTotal(triangle))