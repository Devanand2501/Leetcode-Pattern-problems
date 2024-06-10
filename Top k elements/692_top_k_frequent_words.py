import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        n = len(words)
        if n<k:
            return words
        freq = Counter(words)
        print(freq)
        ans = []
        for i in freq.items():
            heapq.heappush(ans,(i[1],i[0]))
            if len(ans)>k:
                heapq.heappop(ans)
        ans = [word for frequency,word in ans]
        return ans
obj = Solution()
words = ["i","love","leetcode","i","love","coding"]
k = 2
# words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
# k = 4
print(obj.topKFrequent(words,k))