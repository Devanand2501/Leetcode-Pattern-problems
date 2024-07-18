class Solution:
    def solve(self,index,n,slices,end_index):
        if n==0 or index >end_index:
            return 0
        incl = slices[index] + self.solve(index+2,n-1,slices,end_index)
        excl = 0 + self.solve(index+1,n,slices,end_index)
        return max(incl,excl)
    def maxSizeSlices(self, slices: list[int]) -> int:
        n = len(slices)
        inc = self.solve(0,n/3,slices,n-2)
        exc = self.solve(1,n/3,slices,n-1)
        return max(inc,exc)


obj = Solution()
slices = [1,2,3,4,5,6]
print(obj.maxSizeSlices(slices))