class Solution:
    def solve(self,str,pat,i,j):
        # BASE CASE
        if (i<0 and j<0):
            return True

        if (i>=0 and j<0): # abc,bc
            return False

        if (i<0 and j>=0): # abc,***bc OR abc,dabc
            for k in range(j):
                if pat[k] != "*":
                    return False
            return True
        
        # MATCH CASE
        if (str[i] == pat[j] or pat[j] == "?"):
            return self.solve(str,pat,i-1,j-1)
        elif pat[j] == "*":
            return self.solve(str,pat,i-1,j) or self.solve(str,pat,i,j-1)
        else:
            return False
    def isMatch(self, s: str, p: str) -> bool:
        return self.solve(s,p,len(s),len(p))

obj = Solution()
s = "abcde"
p = "a*c?e"
s = "cb"
p = "?a"
print(obj.isMatch(s, p)) 