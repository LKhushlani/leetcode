class Solution:
    

    def longestPalindrome(self, string: str) -> str:
        
        def getPallindromicSubstring(string, startingIdx, endingIdx):
            while startingIdx >=0 and endingIdx < len(string):
                if string[startingIdx] != string[endingIdx]:
                    break
                startingIdx -=1 
                endingIdx += 1


            return [startingIdx+1, endingIdx]
        
        currentString = [0,1]
        for i in range(1,len(string)):
            odd = getPallindromicSubstring(string,i-1,i+1)
            even = getPallindromicSubstring(string,i-1,i)
            longest = max(odd,even, key=(lambda x: x[1] - x[0]))
            currentString = max(currentString,longest, key=lambda x: x[1]- x[0])

        return string[currentString[0] : currentString[1]]