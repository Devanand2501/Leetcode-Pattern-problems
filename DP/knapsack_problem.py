class Solution:
    def solve(self,capacity, wt,value,index):
        if index == 0:
            if wt[0]<=capacity:
                return val[0]
            else:
                return 0
        inc = 0
        if wt[index]<=capacity:
            inc = self.solve(capacity-wt[index], wt,value,index-1) + value[index]
        exc = self.solve(capacity, wt,value,index-1) + 0
        return max(inc,exc)

    def knapSack(self,W, wt, val, n):
        return self.solve(W,wt,val,n-1)

n=3
capacity=4
wt=[4,5,1]
val=[1,2,3]
obj = Solution()
print(obj.knapSack(capacity,wt,val,n))