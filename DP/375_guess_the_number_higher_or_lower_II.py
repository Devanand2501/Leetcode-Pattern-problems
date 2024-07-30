class Solution:
    def solve(self,start,end,memo):
        if start >= end:
            print("Base case")
            return 0
        # if (start,end) in memo:
        #     print("Memoization")
        #     return memo[(start,end)]
        if memo[start][end] != -1:
            print("Memoization")
            return memo[start][end]
        ans = float('inf')
        for i in range(start,end+1):
            ans = min(ans,i+ max(self.solve(start,i-1,memo),self.solve(i+1,end,memo)))
        memo[start][end] = ans
        return memo[start][end] 
    def getMoneyAmount(self, n: int) -> int:
        # memo = {}
        memo = [[-1 for _ in range(n+1)] for _ in range(n+1)]
        return self.solve(1,n,memo)

obj = Solution()
n = 10
print(obj.getMoneyAmount(n)) 