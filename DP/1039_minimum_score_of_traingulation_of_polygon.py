class Solution:
    def solve(self,values,i,j):
        if i+1==j:
            return 0
        ans = float('inf')
        for k in range(i+1,j):
            ans = min(ans,values[i]*values[j]*values[k] +
                        self.solve(values,i,k) +
                        self.solve(values,k,j))
        return ans

    def minScoreTriangulation(self, values: list[int]) -> int:
        n = len(values)
        return self.solve(values,0,n-1)

obj = Solution()
values = [3,7,4,5]
print(obj.minScoreTriangulation(values))