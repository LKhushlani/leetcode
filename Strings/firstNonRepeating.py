def firstNonRepeatingCharacter(string):
    
    charFreq = {}

    for char in string:
        charFreq[char] = charFreq.get(char, 0) + 1

    for char in string:
        if charFreq[char] == 1:
            return char
            

    return -1
    
	
