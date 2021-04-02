def minNumberOfJumps(array):

    if len(array]) == 0:
        return

    steps = array[0]
    maxReach  = array[0] 
    jumps = 0

    for i in range(1, len(array)):
        maxReach = max(maxReach, array[i] + i)
        steps -= 1

        if steps == 0:
            steps = maxReach - i
            jumps += 1

    return jumps +1 