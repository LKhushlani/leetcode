from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [True] + [False] * len(s)

        for idx in range(1, len(s)+1):
            for word in wordDict:
                if dp[idx-len(word)] == True and s[:idx].endswith(word):
                    dp[idx] = True
            print(dp)

        return dp[-1]

            

print(Solution().wordBreak('leetcode', ['leet', 'code']))
        