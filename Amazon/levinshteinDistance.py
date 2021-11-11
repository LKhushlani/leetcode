def levenshteinDistance(str1, str2):
    # Write your code here.
    matrix = [[0 for i in range(len(str2)+1)] for  _ in range(len(str1)+1)]
    print(matrix)
    for i in range(len(str1)+1):
        matrix[i][0] = i
    for i in range(len(matrix[0])):
        matrix[0][i] = i
    print(matrix)
    for i in range(1,len(str1)+1):
        print(str1[i])
        for j in range(1,len(str2)+1):
            print(str1[i-1], str2[j-1])
            if str1[i-1] == str2[j-1]:
                matrix[i][j] = matrix[i-1][j-1]
                print(matrix)
            else:
                print("saksokdso")
                matrix[i][j] = 1 + min(matrix[i][j-1], matrix[i-1][j-1], matrix[i-1][j])
                print(matrix)

    return matrix    


print(levenshteinDistance('abc', 'yabd'))
