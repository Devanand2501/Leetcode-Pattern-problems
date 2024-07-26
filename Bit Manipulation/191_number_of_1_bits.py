class Solution:
    def hammingWeight(self, n: int) -> int:
        num = bin(n)[2:]
        return num.count("1")

obj = Solution()
print(obj.hammingWeight(11))