def longestSubstringWithoutDuplication(string):
    # Write your code here.
    startIdx = 0
    longestSubStr = [0,1]
    hashset  = {}

    for i, char in enumerate(string):
        if char in hashset:
            startIdx = max(startIdx, hashset[char]+1)
        if longestSubStr[1] - longestSubStr[0] <  i+1 - startIdx:
            longestSubStr = [startIdx, i+1]
            
        hashset[char] = i

    return string[longestSubStr[0]: longestSubStr[1]]
        



        






    


		
