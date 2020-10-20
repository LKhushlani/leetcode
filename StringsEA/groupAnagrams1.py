#   time O(w * n logn + n * w logw )
# space  O(wn)   w is no of words and n is length of each word

def groupAnagrams(words):
    # Write your code here.
    sortedWords = ["".join(sorted(word)) for word in words]
    indicies = [i for i in range(len(words))]
    indicies.sort(key = lambda x: sortedWords[x])   # []

	if len(words) == 0:
        return []
    
    result = []
    currentAnagramGroup = []
    currentAnagram = sortedWords[indicies[0]]

    for index in indicies:              
        word = words[index]
        sortedWord = sortedWords[index]

        if currentAnagram  == sortedWord:
            currentAnagramGroup.append(word)
            continue
        
        result.append(currentAnagramGroup)
        currentAnagramGroup = [word]
        currentAnagram = sortedWord

    result.append(currentAnagramGroup)

    return result








        



		
	
	
    
 