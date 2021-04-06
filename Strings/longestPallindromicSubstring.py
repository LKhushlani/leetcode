#  On2 time , On space
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


# def longestPalindromicSubstring(string):
#     longest, currentLongest = 0
    
#     for i in range(1,len(string)):
#         odd = checkPallindrome(string, i-1, i+1)
#         even = checkPallindrome(string, i-1, i)
#         currentlongest = max(odd, even, key = lambda x: x[1]- x[0])
#         longest = max(currentLongest, longest,  key = lambda x: x[1]- x[0])

#     return string[longest[0] : string[longest[1]]]


# def checkPallindrome(string, startIdx, endIdx):
#     while startIdx >=0 and endIdx <= len(string):
#         if string[startIdx] == string[endIdx]:
#             startIdx -=1
#             endIdx += 1 

#         else:
#             break

#     return [startIdx+1, endIdx]








    