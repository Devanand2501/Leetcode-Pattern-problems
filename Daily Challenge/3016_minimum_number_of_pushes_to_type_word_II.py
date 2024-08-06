class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = {}
        n = len(word)
        for i in range(n):
            counter[word[i] ] = counter.get(word[i],0) + 1
        lst = []
        for k,v in counter.items():
            lst.append((k,v))
        lst.sort(key=lambda x:x[1],reverse=True)
        print(lst)
        ans = 0
        count = 0
        for i in range(len(lst)):
            count += 1
            if count > 8:
                if count % 8 == 0:
                    mul = count //8
                    ans += lst[i][1] * (mul)
                    continue
                mul = count //8
                ans += lst[i][1] * (mul + 1)
            else:
                ans += lst[i][1]
        return ans
word = "xyzxyzxyzxyz"
word = "abcde"
word = "aabbccddeeffgghhiiiiii"
obj = Solution()
print(obj.minimumPushes(word))  