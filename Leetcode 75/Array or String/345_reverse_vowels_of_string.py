class Solution:
    def reverseVowels(self, s: str) -> str:
        dp = []
        vowels = ['a','i','e','o','u']
        n = len(s)
        for i in range(n):
            if s[i] in vowels:
                dp.append(i)
        print(dp)
        dp.sort(reverse=True)
        res = ''
        j = 0
        for i in range(n):
            if i in dp:
                res += s[dp[j]]
                j+=1
            else:
                res+= s[i]
        return res

obj = Solution()
s = "hello"
print(obj.reverseVowels(s))