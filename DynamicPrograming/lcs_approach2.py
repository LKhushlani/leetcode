# O(mn) time | same for space
def longestCommonSubsequence(str1, str2):
    lcs = [[[None, 0, None, None] for i in range(len(str1) + 1)] for j in range(len(str2) + 1)]
    # [ if we will include current char , len of lcs till now, index of current sequence (i), index of current sequence (i)]
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str1[j - 1] == str2[i - 1]:
                lcs[i][j] = [str2[i - 1], lcs[i - 1][j - 1][1] + 1, i - 1, j - 1]
            else:
                if lcs[i][j - 1][1] > lcs[i - 1][j][1]:
                    lcs[i][j] = [None, lcs[i][j - 1][1], i, j - 1]

                else:
                    lcs[i][j] = [None, lcs[i - 1][j][1], i - 1, j]

    return buildSequence(lcs)


def buildSequence(lcs):
    sequence = []
    i = len(lcs) - 1
    j = len(lcs[0]) - 1
    while i != 0 and j != 0:
        currentEntry = lcs[i][j]
        if currentEntry[0] is not None:
            sequence.append(currentEntry[0])
        i = currentEntry[2]
        j = currentEntry[3]

    return list(reversed(sequence))