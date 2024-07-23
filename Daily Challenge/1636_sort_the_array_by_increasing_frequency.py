from typing import Counter,List
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        print(counter)
        ans = []
        for key, value in sorted(counter.items(),key= lambda x:(x[1],-x[0])):
            print(key,value)
            for i in range(value):
                ans.append(key)
        return ans

obj = Solution()
nums = [1,1,2,2,2,3]
nums = [2,3,1,3,2]
print(obj.frequencySort(nums))