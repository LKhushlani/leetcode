def longestPalindromicSubstring(string):
    # Write your code here.

    currentLongest = [0,1]
    for i in range(1, len(string)):
        odd = getPalindromicSubstring(string, i-1, i+1)
        even = getPalindromicSubstring(string, i-1, i)
        longest = max(odd, even , key = lambda x: x[1]- x[0])
        currentLongest = max(currentLongest, longest, key = lambda x: x[1]-x[0])

    return string[currentLongest[0]: currentLongest[1]]

def getPalindromicSubstring(string, leftIndex, rightIndex):

    while leftIndex >= 0 and rightIndex < len(string):
        if string[leftIndex] != string[rightIndex]:
            break
        leftIndex -=1 
        rightIndex += 1 

    return [leftIndex+1, rightIndex]

    