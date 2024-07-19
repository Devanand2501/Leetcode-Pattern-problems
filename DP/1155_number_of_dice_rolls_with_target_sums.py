import time 
start_time = time.time()
class Solution:
    def solve(self,n,k,x):
        if x < 0: # target is < 0
            return 0
        
        if n == 0 and x !=0: # target not reached but dice are over
            return 0

        if x == 0 and n !=0: # target reached but dice are still present
            return 0
        
        if n == 0 and x == 0:
            return 1
        
        ans = 0
        for i in range(1,k+1):
            ans += self.solve(n-1,k,x-i)
        return ans 

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        return self.solve(n,k,target)

obj = Solution()
n = 2
k = 6
target = 7

# n = 30
# k = 30
# target = 500
print(obj.numRollsToTarget(n,k,target))
end_time = time.time()
print("Time taken:", end_time - start_time)