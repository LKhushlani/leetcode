def longestCommonSubsequence(str1, str2):

    subsequence = [[[] for i in range(len(str1)+1)] for j in range(len(str2)+1)]

    for i in range(1, len(str2)+1):
        for j in range(1, len(str1)+1):
            if str2[i-1] == str1[j-1]:
                subsequence[i][j] = subsequence[i-1][j-1] + [str1[i-1]]
            else:
                subsequence[i][j] = max(subsequence[i-1][j], subsequence[i][j-1], key=len)

    return subsequence[-1][-1]
print(longestCommonSubsequence('ZXVVYZW', 'XKYKZPW'))