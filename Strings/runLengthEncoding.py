def runLengthEncoding(string):
    # Write your code here.
    cur_count = 1
    cur_char = string[0]
    result = ''
    for i in range(len(string)):
        cur_char = string[i]
        prev_char = string[i-1]
		
		if cur_count == 9 or prev_char != cur_char:
			result += str(cur_count) + char
			cur_count = 0 
		cur_count += 1

    result += str(cur_count) + cur_char
	return result

# runLengthEncoding("AAAAAAAAAAAAABBCCCCDD")