from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [True] + [False] * len(s)
        for idx in range(1,len(s)+1):
            print("idx", idx)
            for word in wordDict:
                print(word)
                print(dp)
                if dp[idx-len(word)] == True and s[:idx].endswith(word):
                    dp[idx] = True

        return dp[-1]


s  = Solution().wordBreak('leetcode', ['leet', 'code'])
print(s)


        
        