class Solution:
    ''' RECURSION + MEMOIZATION
    '''
    def solve(self,text1,text2):
        curr = [0] * (len(text2)+1)
        next = [0] * (len(text2)+1)
        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if text1[i]==text2[j]:
                    ans = 1 + next[j+1]
                else:
                    ans = max(next[j],curr[j+1])
                curr[j] = ans
            next = curr[:]
        return next[0]
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.solve(text1,text2)
obj = Solution()
text1 = "abcde"
text2 = "ace" 
print(obj.longestCommonSubsequence(text1, text2))  