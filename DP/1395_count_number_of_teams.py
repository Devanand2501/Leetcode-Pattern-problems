from typing import List

class Solution:
    def solve(self, rating: List[int], index: int, count:int, last_rating: int, direction: int) -> int:
        if count == 3:
            return 1
        if index >= len(rating):
            return 0
        # print("Index-->",index,"--","count-->",count)
        total = 0
        if (direction == 0 and rating[index] > last_rating) or \
               (direction == 1 and   rating[index] < last_rating):
                print("Include ==> Index-->",index,"--","count-->",count,"num-->",rating[index])
                total += self.solve(rating, index+1, count + 1, rating[index],direction)
        print("Exclude ==> Index-->",index,"--","count-->",count,"num-->",rating[index])
        total += self.solve(rating, index+1, count, last_rating,direction)
        return total

    def numTeams(self, rating: List[int]) -> int:
        return self.solve(rating, 0,0,float('-inf'), 0) + self.solve(rating, 0,0,float('inf'), 1)

obj = Solution()
rating = [2,5,3,4,1]
print(obj.numTeams(rating))  # Output: 3