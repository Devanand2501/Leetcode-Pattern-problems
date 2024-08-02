class Solution:
    ''' RECURSION + MEMOIZATION
    '''
    def solve(self,text1,text2):
        dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if text1[i]==text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                    return dp[i][j]
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j+1])
        return dp[0][0]
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.solve(text1,text2)
obj = Solution()
text1 = "abcde"
text2 = "ace" 
print(obj.longestCommonSubsequence(text1, text2))  