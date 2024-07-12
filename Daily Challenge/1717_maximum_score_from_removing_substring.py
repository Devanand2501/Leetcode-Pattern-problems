from collections import defaultdict

class Solution:
    ''' RECURSION + MEMOIZATION
    def solve(self,s,x,y,dp):
        if s.find("ab") == -1 and s.find("ba") == -1:
            return 0
        indexab = s.find("ab")
        indexba = s.find("ba")
        ab = 0
        ba = 0
        if s in dp:
            return dp[s]
        if indexab != -1:
            ab = self.solve(s[:indexab]+s[indexab+2:],x,y,dp) + x
        if indexba != -1:
            ba = self.solve(s[:indexba]+s[indexba+2:],x,y,dp) + y
        dp[s] = max(ab,ba)
        return dp[s]
    '''
    def maximumGain(self, s: str, x: int, y: int) -> int:
        total_score = 0
        high_priority_pair = "ab" if x > y else "ba"
        low_priority_pair = "ba" if high_priority_pair == "ab" else "ab"

        string_after_first_pass = self.remove_substring(s, high_priority_pair)
        removed_pairs_count = (len(s) - len(string_after_first_pass)) // 2

        total_score += removed_pairs_count * max(x, y)

        string_after_second_pass = self.remove_substring(
            string_after_first_pass, low_priority_pair
        )
        removed_pairs_count = (
            len(string_after_first_pass) - len(string_after_second_pass)
        ) // 2

        total_score += removed_pairs_count * min(x, y)

        return total_score

    def remove_substring(self, input: str, target_pair: str) -> str:
        while input.find(target_pair) != -1:
            index = input.find(target_pair)
            input = input[:index] + input[index+2:]
        return input 

s = "aabbaaxybbaabb"
x = 5
y = 4
print(Solution().maximumGain(s,x,y))