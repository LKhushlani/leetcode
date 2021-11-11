def levenshteinDistance(str1, str2):
    # Write your code here.
    distanceMatrix = [[0 for x in range(len(str2)+1)] for j in range(len(str1)+1)]
    for i in range(len(str1)+1):
        distanceMatrix[i][0] = i
    for i in range(len(str2)+1):
        distanceMatrix[0][i] = i

    for i in range(1,len(str1)+1):
        for j in range(1, len(str2)+1):
            if str1[i-1] == str2[j-1]:
                distanceMatrix[i][j]=distanceMatrix[i-1][j-1]
            else:
                distanceMatrix[i][j] = 1 + min(distanceMatrix[i-1][j-1], distanceMatrix[i-1][j], distanceMatrix[i][j-1])

	return distanceMatrix[-1][-1]