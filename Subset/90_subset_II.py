class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = [[]]

        for i in nums:
            sub = []
            print("res",res)
            for j in res:
                if j+[i] not in res:
                    sub.append(j+[i])
            print("sub",sub)
            res.extend(sub)
        return res

obj = Solution()
nums = [1,2,2]
print(obj.subsetsWithDup(nums))