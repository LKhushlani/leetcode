class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        
        index = float('-inf')
        ans = [-1 for i in S]
        res = [0 for char in S]
        for i,char in enumerate(S):
            if char == C:
                index = i
            if i>= index:
                ans[i] = i-index
        for i in range(len(S)-1, -1,-1):
            if S[i] == C:
                index = i
            if i < index:
                if ans[i] > index-i:
                    ans[i] = index-i
        return ans
