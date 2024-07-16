class Solution:
    def solve(self,score, index, time):
        if index == len(score):
            return 0
        inc = score[index] * (time + 1) + self.solve(score,index + 1, time + 1)
        exc = self.solve(score,index + 1, time)
        return max(inc,exc)
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        n = len(satisfaction)
        satisfaction.sort()
        return self.solve(satisfaction,0,0)

obj = Solution()
print(obj.maxSatisfaction([-1,-8,0,5,-9]))